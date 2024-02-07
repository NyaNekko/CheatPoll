from pyrogram import filters

from CheatPollBot import app, OWNER
from CheatPollBot.modules.database import *

@app.on_message(filters.command("botchk") & filters.user(OWNER))
async def dbtool(_, message):
    xx = all_users()
    x = all_groups()
    await message.reply_text(text=f"""
~ Bot Stats
🙋‍♂️ Users : `{xx}`
👥 Groups : `{x}`
""")
    
@app.on_message(filters.command("users") & filters.user(OWNER))
async def dbtool(_, message):
    userIds = all_users_ids()
    await message.reply_text(text=f"""
~ Bot Stats
🙋‍♂️ Users : `{userIds}`
""")
    
@app.on_message(filters.command("grps") & filters.user(OWNER))
async def dbtool(_, message):
    grpIds = all_groups_ids()
    await message.reply_text(text=f"""
~ Bot Stats
👥 Groups : `{grpIds}`
""")
