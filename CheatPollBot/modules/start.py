from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from CheatPollBot import app, BOT_USERNAME

@app.on_message(filters.command('start'))
async def start_message(_, message):
    if message.chat.type.value == "channel":
       return
    userName = message.from_user.mention
    if message.chat.type.value == "private":
      await message.reply_photo("https://telegra.ph/file/ba0f9ae316808e74fb73b.jpg",caption=f"""
**Hello {userName} !**
**This Bot Can Reveal Quiz Poll Answers Easily 😊! You Can Use /help To Know The Usage**

**__NOTE: It Only Supports PM For Now__**
""", reply_markup=InlineKeyboardMarkup([
    [
        InlineKeyboardButton("➕ Add To Group", url=f"https://t.me/{BOT_USERNAME}?startgroup=start=invite_users")
    ],
    [
        InlineKeyboardButton("SUPPORT", url="https://t.me/EpixeaSupport"),
        InlineKeyboardButton("UPDATES", url="https://t.me/Epixea")
    ],
    [
        InlineKeyboardButton("DEVELOPER", user_id=5556628090)
    ]
]))
    else:
       await message.reply_photo("https://telegra.ph/file/ba0f9ae316808e74fb73b.jpg",caption=f"""
**Hello {userName} !**
**This Bot Can Reveal Quiz Poll Answers Easily 😊! You Can Use /help To Know The Usage**
""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("START", url=f"https://t.me/{BOT_USERNAME}?start")]]))
       

@app.on_message(filters.command('help'))
async def help_message(_, message):
   await message.reply("""
**➕ Help Section:**
**└** If You Want Quiz Poll Answer In Group, Reply /poll Command On Quiz.
                       
**└** If You Want Quiz Poll Answer In Your PM, Just Forward The Poll To Bots PM
                       
**🤖 IF YOU FACE ANY DIFFICULTIES OR ISSUE REGARDING BOT YOU CAN CONTACT ADMINS OF BOT @EpixeaSupport**
""")