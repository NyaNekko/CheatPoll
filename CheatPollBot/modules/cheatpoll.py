from pyrogram import filters
from pyrogram.enums import PollType
from pyrogram.errors import RevoteNotAllowed

from CheatPollBot import app, user

@app.on_message(filters.command("poll"), group=10)
@user.on_message(filters.command("poll"))
async def pollCheat(_, message):
    if message.reply_to_message.poll.type == PollType.QUIZ:
        pollID = message.reply_to_message.id
        try:
          a = await user.vote_poll(message.chat.id, message.reply_to_message.id, 0)
          correctAnswer = a.correct_option_id
          answer = a.options[correctAnswer].text
          await message.reply_text(f"The Correct Answer Of The Poll Is: {answer}")
        except RevoteNotAllowed:
           a = await user.get_messages(message.chat.id, pollID)
           correctAnswer = a.poll.correct_option_id
           answer = a.poll.options[correctAnswer].text
           await message.reply_text(f"The Correct Answer Of The Poll Is: {answer}")