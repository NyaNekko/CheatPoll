from pyrogram import filters
from pyrogram.enums import PollType
from pyrogram.errors import RevoteNotAllowed, MessageIdInvalid

from CheatPollBot import app, user
from CheatPollBot.modules.database import *

@app.on_message(filters.command("poll"), group=10)
async def pollCheat(_, message):
    if message.reply_to_message.poll.type == PollType.QUIZ:
      a = message.reply_to_message
      add_user(message.from_user.id)
      b = await user.forward_messages("ewaifusupport", a.chat.id, a.id)
      try:
        c = await user.vote_poll(b.chat.id, b.id, 0)
        correctAnswer = c.correct_option_id
        answer = c.options[correctAnswer].text
        await message.reply_text(f"The Correct Answer Of The Poll Is: {answer}")
      except RevoteNotAllowed:
         c = await user.get_messages(b.chat.id, b.id)
         correctAnswer = c.poll.correct_option_id
         answer = c.poll.options[correctAnswer].text
         await message.reply_text(f"The Correct Answer Of The Poll Is: {answer}")

@app.on_message(filters.private, group=11)
async def pollCheatPm(_, message):
   if not message.poll:
      return
   if message.poll.type == PollType.QUIZ:
      add_user(message.from_user.id)
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
