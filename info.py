# (c) @biisal
from os import getenv
import re

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "1562935405"))
API_ID = int(getenv("API_ID", "25833520"))
API_HASH = str(getenv("API_HASH", "7d012a6cbfabc2d0436d7a09d8362af7"))
BOT_TOKEN = str(getenv("BOT_TOKEN", "6537146254:AAEsbF-TiOwbD4-vWS19Amjgc_21VeocaPM"))
MONGO_DB = str(
    getenv(
        "MONGO_DB",
        "mongodb+srv://trumbot:trumbot@cluster0.cfkaeno.mongodb.net/?retryWrites=true&w=majority",
    )
)
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b><a href='telegram.me/THE_DS_OFFICIAL'>{file_caption} Telegram : @THE_SILENT_TEAMS\n\nForward the file before Downloading.</a></b>",
    )
)
