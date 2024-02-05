import os
import asyncio
import sys
import traceback
import aiofiles
from io import BytesIO, StringIO

from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
)

from CheatPollBot import app, OWNER


task_list: list = []

@app.on_callback_query(filters.regex("pytaskcallback_"))
async def py_taskcallback(_, callback: CallbackQuery):
    """Callback for shell command."""

    if callback.from_user.id != callback.message.reply_to_message.from_user.id:
        return await callback.answer(
            "That command is not initiated by you.", show_alert=True)

    task_index = callback.data.split("_")[-1]
    message = callback.message

    task = task_list[int(task_index)]

    if not task.done():
        task.cancel()
        task_list.remove(task)

    return await message.edit("Task Killed Successfully.")


async def aexec(code, client, message):
    exec(
        "async def __aexec(client, message): "
        + "".join(f"\n {a}" for a in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)


async def py_runexec(client: Client, message: Message, replymsg: Message):
    """Run Python Code inside Telegram"""

    old_stderr = sys.stderr
    old_stdout = sys.stdout

    redirected_output = sys.stdout = StringIO()
    redirected_error = sys.stderr = StringIO()

    stdout = None
    stderr = None
    exception = None

    refresh_button = InlineKeyboardMarkup(
        [[InlineKeyboardButton("Refresh  🔄", callback_data="refresh")]]
    )

    try:
        code = message.text.split(maxsplit=1)[1]
    except IndexError:
        return await replymsg.edit(
            "No codes found to execute.", reply_markup=refresh_button)

    try:
        task = asyncio.create_task(aexec(code, client, message))
        task_list.append(task)

        button = [
            [
                InlineKeyboardButton(
                    "Kill Process",
                    callback_data=f"pytaskcallback_{task_list.index(task)}",
                )
            ]
        ]
        await replymsg.edit("Executing...", reply_markup=InlineKeyboardMarkup(button))
        await task
        task_list.remove(task)

    except Exception:
        exception = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    evaluation = ""
    if exception:
        evaluation = f"--**Exception**--\n\n`{exception}`"
    elif stderr:
        evaluation = f"--**Error**--\n\n`{stderr}`"
    elif stdout:
        evaluation = f"--**Output**--\n\n`{stdout}`"
    else:
        evaluation = "success"
    final_output = f"{evaluation.strip()}"

    if len(final_output) > 4000:
        async with aiofiles.open("output.txt", "w+", encoding="utf8") as file:
            await file.write(str(evaluation.strip()))

        await replymsg.edit(
            "output too large. sending it as a file...", reply_markup=refresh_button)

        await client.send_document(message.chat.id, "output.txt", caption="output.txt")
        os.remove("output.txt")

    return await replymsg.edit(
        final_output, reply_markup=refresh_button)


@app.on_callback_query(filters.regex("refresh"))
async def py_callback(client: Client, callbackquery: CallbackQuery):
    clicker_user_id = callbackquery.from_user.id
    message_user_id = callbackquery.message.reply_to_message.from_user.id

    if clicker_user_id != message_user_id:
        return await callbackquery.answer(
            "That command is not initiated by you.", show_alert=True)

    replymsg = callbackquery.message
    message = await client.get_messages(
        callbackquery.message.chat.id, callbackquery.message.reply_to_message.id)

    if callbackquery.data == "refresh":
        await py_runexec(client, message, replymsg)


@app.on_message(filters.command(["e", "eval"]) & filters.user(OWNER))
async def py_execute(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text(
            "**Usage:** Executes python commands directly via bot.\n\n**Example: **<pre>/exec print('hello world')</pre>")
    else:
        replymsg = await message.reply_text("Executing..", quote=True)
        await py_runexec(client, message, replymsg)



@app.on_message(filters.command("update") & filters.user(OWNER))
async def update(_, message: Message):
    msg = await message.reply_text("Pulling changes with latest commits...", quote=True)
    os.system("git pull")
    await msg.edit("Changes pulled with latest commits. Restarting bot now... ")
    os.execl(sys.executable, sys.executable, "-m", "CheatPollBot")
