#BOT INSTANCE CODE

import time
from logging import ERROR, INFO, StreamHandler, basicConfig, getLogger, handlers
import pytz
from pyromod import Client

from CheatPollBot.Config import (
    API_HASH,
    API_ID,
    BOT_TOKEN,
    TIMEZONE,
    DB_URI,
    SESSION,
    OWNER
)

#LOGGER SETUP
basicConfig(
    level=INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s.%(funcName)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        handlers.RotatingFileHandler("logs.txt", mode="w+", maxBytes=1000000),
        StreamHandler(),
    ],
)
getLogger("pyrogram").setLevel(ERROR)


# --------------------------------- #

MOD_LOAD = []
MOD_NOLOAD = []
HELPABLE = {}
start = time.time()
TIME_ZONE = pytz.timezone(TIMEZONE)

# --------------------------------- #

# SET UP THE BOT CLIENT
app = Client(
    "f2link",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# SET UP THE BOT CLIENT
user = Client(
    "userf",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string = SESSION
)

# START THE CLIENT AND GET INFO
app.start()
user.start()

BOT_ID = app.me.id
BOT_NAME = app.me.first_name
BOT_USERNAME = app.me.username
