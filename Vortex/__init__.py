from requests import get
import pylast
import asyncio
from distutils.util import strtobool as sb
from logging import basicConfig, getLogger, INFO, DEBUG
import os
import sys
from telethon.sessions import StringSession
from telethon import TelegramClient
from Vortex.Config import Var
import time
from telethon.tl import functions
from telethon.tl.functions.channels import JoinChannelRequest as Jcr, LeaveChannelRequest as Lcr


async def VorteX():
   global bot
   
   if Var.STRING_SESSION:
       rizz = str(Var.STRING_SESSION)
       print("Starting Session.....")
       bot = TelegramClient(StringSession(rizz), Var.APP_ID, Var.API_HASH)
       try:
           await bot.start()
           botme = await bot.get_me()
           await bot(Jcr(channel="@VortexUB"))
           await bot(Jcr(channel="@VorteXUbSupport"))
       except Exception as e:
           print(e)
           pass
   else:
       rizz = "VortexBot"
       bot = TelegramClient(rizz, Var.APP_ID, Var.API_HASH)
       try:
          await bot.start()
       except Exception as e:
          pass


loop = asyncio.get_event_loop()
loop.run_until_complete(VorteX())


StartTime = time.time()
Vortexversion = "1.0.1"

CMD_LIST = {}
CMD_HELP = {}
INT_PLUG = ""
LOAD_PLUG = {}
CMD_HNDLR = Var.CMD_HNDLR

ENV = os.environ.get("ENV", False)
""" PPE initialization. """

# Bot Logs setup:
if bool(ENV):
    CONSOLE_LOGGER_VERBOSE = sb(
        os.environ.get(
            "CONSOLE_LOGGER_VERBOSE",
            "False"))

    if CONSOLE_LOGGER_VERBOSE:
        basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=DEBUG,
        )
    else:
        basicConfig(
            format="✘ %(asctime)s ✘ - ⫸ %(name)s ⫷ - ⛝ %(levelname)s ⛝ - ║ %(message)s ║",
            level=INFO)
    LOGS = getLogger(__name__)
    
    CONFIG_CHECK = os.environ.get(
        "___________PLOX_______REMOVE_____THIS_____LINE__________", None)

    if CONFIG_CHECK:
        LOGS.info(
            "Please remove the line mentioned in the first hashtag from the config.env file"
        )
        quit(1)

    # Logging channel/group configuration.
    BOTLOG_CHATID = os.environ.get("BOTLOG_CHATID", None)
    try:
        BOTLOG_CHATID = int(BOTLOG_CHATID)
    except BaseException:
        pass

    # Userbot logging feature switch.
    BOTLOG = sb(os.environ.get("BOTLOG", "False"))

    
    PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))

    # Console verbose logging
    CONSOLE_LOGGER_VERBOSE = sb(
        os.environ.get(
            "CONSOLE_LOGGER_VERBOSE",
            "False"))

    # SQL Database URI
    DB_URI = os.environ.get("DATABASE_URL", None)

    # OCR API key
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)

    # remove.bg API key
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)

    # Chrome Driver and Headless Google Chrome Binaries
    CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)
    GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)

    # For bit.ly plugin
    BITLY_TOKEN = os.environ.get("BITLY_TOKEN", None)

    # OpenWeatherMap API Key
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)

    # Anti Spambot Config
    ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))

    ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))

    # Youtube API key
    YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)

    # Default .alive name
    ALIVE_NAME = os.environ.get("ALIVE_NAME", None)

    # for Autopic
    AUTOPIC_TEXT = os.environ.get(
        "AUTOPIC_TEXT",
        "Life Is too Short.\n And so is your TG account.")
    AUTO_PIC_FONT = os.environ.get("AUTOPIC_FONT", "vortex.ttf")
    AUTOPIC_FONT_COLOUR = os.environ.get("AUTOPIC_FONT_COLOUR", None)

    CMD_HNDLR = os.environ.get("CMD_HNDLR", r"\.")

    LESS_SPAMMY = os.environ.get("LESS_SPAMMY", True)

    # Time & Date - Country and Time Zone
    COUNTRY = str(os.environ.get("COUNTRY", ""))

    TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))

    # Clean Welcome
    CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))

    # CUSTOM PMPERMIT
    CUSTOM_PMPERMIT = os.environ.get("CUSTOM_PMPERMIT", None)

    # PMPERMIT
    COUNT_MSG = 0
    COUNT_PM = {}

    # Last.fm Module
    BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
    DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)

    LASTFM_API = os.environ.get("LASTFM_API", None)
    LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
    LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
    LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
    LASTFM_PASS = pylast.md5(LASTFM_PASSWORD_PLAIN)
    if not LASTFM_USERNAME == "None":
        lastfm = pylast.LastFMNetwork(api_key=LASTFM_API,
                                      api_secret=LASTFM_SECRET,
                                      username=LASTFM_USERNAME,
                                      password_hash=LASTFM_PASS)
    else:
        lastfm = None

    # Google Drive Module
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY",
                                             "./downloads")
else:
    # Put your vars here ,Only if using local host
    PLACEHOLDER = None


# Global Variables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
ISAFK = False
AFKREASON = None

