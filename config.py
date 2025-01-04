import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "25762898"))
API_HASH = getenv("API_HASH", "c4a5cb2db3f3d4a52de7689c4d9f2812")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7788838360:AAFmOjFvgo9Cu7TEdZ2-FRu8JQr09K8F42E")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://architect04:architect04@cluster0.fylqb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002329626146"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7941950690"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/jiosaavnmusic/JioSaavn",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/beast_fox_network")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/denkimusic")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "800"))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 904857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 9073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQGJHFIAUCzOCpvYE4f3nncGp7AgqvZ-xSVl2sRn1Cz9SSUTatBuZaCYStQZdlUumZkgvLvrShsuInAlI3gA_KdHX6tUW_bPjk-WxO_yHT5-Q0JbWiAlV1Ae1ax3gkR37CujsE0opqlmEhxrTh7Y1WPLO2DyeIrcGnXq8-1fmOtn6xCzv2OWD-DS57lKFf17HdiHEWmdMoZih988TEhJKDBgkNUw5n1byUE5YBqLBeNY9LH82aV6TcLxTiWK3j2QZ6U7A21YssRJnmNozk6uVT-7jPWpAgbZG1BpJqfzoNwKwM-WiIVZ9XpNKJcZHvC9n10TjtSoktEXm0KcP3NB9upfByxNwgAAAAGpEg3QAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://envs.sh/rSy.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://envs.sh/rSy.jpg"
)
PLAYLIST_IMG_URL = "https://envs.sh/rSy.jpg"
STATS_IMG_URL = "https://envs.sh/rSy.jpg"
TELEGRAM_AUDIO_URL = "https://envs.sh/rSy.jpg"
TELEGRAM_VIDEO_URL = "https://envs.sh/rSy.jpg"
STREAM_IMG_URL = "https://envs.sh/rSy.jpg"
SOUNCLOUD_IMG_URL = "https://envs.sh/rSy.jpg"
YOUTUBE_IMG_URL = "https://envs.sh/rSy.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://envs.sh/rSy.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://envs.sh/rSy.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://envs.sh/rSy.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 800**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
)
