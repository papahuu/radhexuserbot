import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "20054364")) #optional
API_HASH = getenv("API_HASH", "6a9a4fbda55762023c32133f76cbc1d1") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5738579437").split()))
OWNER_ID = int(getenv("OWNER_ID", "8093150680"))
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN", "")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://envs.sh/620.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP","-1002458103093")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/papahuu/radhexuserbot")
BRANCH = getenv("BRANCH", "main") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
