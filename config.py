import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "14050586"))
API_HASH = getenv("API_HASH", "42a60d9c657b106370c79bb0a8ac560c")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7229854636:AAG6Ce0HYkigextzo34xMPyWsCOxOdtcz10")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://architect04:architect04@cluster0.fylqb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002415603391"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7078122796"))

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
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Team_Hypers_Networks")

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
STRING1 = getenv("STRING_SESSION", "BQGh1p0AX3wrERiE8tQM56PRRsYBTVDtXs8PyFmvHXxnw62LvnliF1U_Pv_AV2wJO9--2z2E7ag_HC2jPFAqb1X2ah-18xWbyK3L-MVwR2xFzrjhSbA-VVa0daupUjTm51KuLP24_AdugdVraQ5uDKTo89bjZgZpTwak4xwSQNdSid0_0XR39ChAkiqPIpnz8WKICbfkIoKt4Q4xBl8fvDLWRBgPgLIwC52ZZ1u50XJSaPI6NRnB4MiVvlF1vkSGloWHsUm3rkjTFudNF8dU6aQHtpSuHc74HDV1Od0Sb5Gipao9uSKiwMUkhGlcAeSxZ3KsQWBrW-LgNyKJExhwV_n21bv1wQAAAAGzf77iAA")
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
    "START_IMG_URL", "https://envs.sh/sE4.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://envs.sh/sE4.jpg"
)
PLAYLIST_IMG_URL = "https://envs.sh/sE4.jpg"
STATS_IMG_URL = "https://envs.sh/sE4.jpg"
TELEGRAM_AUDIO_URL = "https://envs.sh/sE4.jpg"
TELEGRAM_VIDEO_URL = "https://envs.sh/sE4.jpg"
STREAM_IMG_URL = "https://envs.sh/sE4.jpg"
SOUNCLOUD_IMG_URL = "https://envs.sh/sE4.jpg"
YOUTUBE_IMG_URL = "https://envs.sh/sE4.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://envs.sh/sE4.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://envs.sh/sE4.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://envs.sh/sE4.jpg"


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
