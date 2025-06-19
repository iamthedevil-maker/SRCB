#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", 1604400, cast=int)
API_HASH = config("API_HASH", "8e6598bb138e8e7890b0fa19d6a152f6")
BOT_TOKEN = config("BOT_TOKEN", "6913900666:AAG10rF8yObVKPe29jccOC62D90KEcdJh2g")
SESSION = config("SESSION", "BQAYezAAY2SK7qw2eWmYPLq0sqggdVp60DZPHNnr_lqQt6zwdi_iWQunaWwiQZQpqDIXFfEkXK6Np5226DU6rim6QJKUIofq-U_z5dts7JJm1SEZIU84rrWFOB1947yI96HdAzHBN5bHNdZyjHZwuOwENd257QLnSrWW1NAd40D_gNr-Dhvxt3wqIirOlXqFiVanw5ymqPTxWgXYl7LbZ-2z0P5Eanp0oztBAMe-5heaBXuUUgaUvmTWXJeCxe3dBaW-kQVDf08_Hdo71IjSkBbbOs37H58FIUHhw-NkY4HhHY-4Q9NEk1cBAtnN06KqIlEmutmJbpMBiLX-v9hfRPuUca2G1AAAAAGfciwdAA")
FORCESUB = config("FORCESUB", "hellchatdd")
AUTH = config("AUTH", 6970027037, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
