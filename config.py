import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
MONGODB_URL = getenv("MONGODB_URL")
OWNER_NAME = getenv("OWNER_NAME")
ALIVE_NAME = getenv("ALIVE_NAME")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "gecepayizi")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Rahid_44")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://images.app.goo.gl/QSkHkYEFsXW4xR2z5")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "100"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO")
IMG_1 = getenv("IMG_1", "https://images.app.goo.gl/QSkHkYEFsXW4xR2z5")
IMG_2 = getenv("IMG_2", "https://images.app.goo.gl/QSkHkYEFsXW4xR2z5")
IMG_3 = getenv("IMG_3", "https://images.app.goo.gl/QSkHkYEFsXW4xR2z5")
IMG_4 = getenv("IMG_4", "https://images.app.goo.gl/QSkHkYEFsXW4xR2z5")
IMG_5 = getenv("IMG_5", "https://images.app.goo.gl/QSkHkYEFsXW4xR2z5")
