from pyrogram import filters
from pyrogram.enums import PollType
from pyrogram.errors import RevoteNotAllowed

from CheatPollBot import app, user

@app.on_message(filters.command("poll"), group=10)
async def pollCheat(_, message):
    await message.reply("Due To Some Reasons The Bot Only Works In PM.\n\n**Forward The Poll To Bots PM 😊**")

@app.on_message(filters.private)
async def pollCheatPm(_, message):
   if message.poll:
      a = await message.forward("ewaifusupport")
      try:
        b = await user.vote_poll(a.chat.id, a.id, 0)
        correctAnswer = b.correct_option_id
        answer = b.options[correctAnswer].text
        await message.reply_text(f"The Correct Answer Of The Poll Is: {answer}")
      except RevoteNotAllowed:
         b = await user.get_messages(a.chat.id, a.id)
         correctAnswer = b.poll.correct_option_id
         answer = b.poll.options[correctAnswer].text
         await message.reply_text(f"The Correct Answer Of The Poll Is: {answer}")
