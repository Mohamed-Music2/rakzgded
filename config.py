## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BAB-3PLsIDRarXyJ06CUFNEb14EGSTLK88inr0UlJK9d3GgSuTP4IpGcYAzmhGXr0P3j3KQZEqbj9EQ22vt3TnkawThnk3ijNSjXCbXKIaEKWTRuibJSQezppdRazoBVU7k3e7CUp2SFl42cuvTIlxocbxYqno9ehn_6KFvlL5XCBT9Uzq4rCWOQ8mNVth3hD8beHETYeE7hUPCcNh0NICv5RsstPCubms5U8sYcG4RbLmcaqqvtNuv4pk2zT3yPJXcF9muWUe434XXZjQViz4PcR7vxCNBhD4xRcmNWyIfXlSLcvjtSXsnps1ojEHxyy7xTv5vDGniimTPBZGiVJbEPAAAAAS2FcekA")
BOT_TOKEN = getenv("BOT_TOKEN", "5409818512:AAHNVmbdbgAV_NBWmRl3cpU7Wpp2rWDzpz4")
BOT_NAME = getenv("BOT_NAME", "- 𝚃𝙰𝙴𝙼 𝙴𝙸𝚂𝙰 𝙼𝚄𝚂𝙸𝙲 ‹𝟹 .")
API_ID = int(getenv("API_ID", "16050450"))
API_HASH = getenv("API_HASH", "0dd89e225b6ddd6f03e8135460d31177")
OWNER_NAME = getenv("OWNER_NAME", " 🇩🇪ؖؖؖؖؖؖؖؖؖؖ𓆩『𖤍𝑬𝑰𝑺𝑨㉨』𝑴𝑶𝑯𝑨𝑴𝑬𝑫𓆪ؖؖؖؖؖؖؖؖؖ✹ ⃝⃙𓆩™")
OWNER_USERNAME = getenv("OWNER_USERNAME", "lMl4ll")
ALIVE_NAME = getenv("ALIVE_NAME", "🇩🇪ؖؖؖؖؖؖؖؖؖؖ𓆩『𖤍𝑬𝑰𝑺𝑨㉨』𝑴𝑶𝑯𝑨𝑴𝑬𝑫𓆪ؖؖؖؖؖؖؖؖؖ✹ ⃝⃙𓆩™")
BOT_USERNAME = getenv("BOT_USERNAME", "lMl4ll_MUSIC_BOT")
OWNER_ID = getenv("OWNER_ID", "5191100896")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "- 𝚃𝙰𝙴𝙼 𝙴𝙸𝚂𝙰 𝙼𝚄𝚂𝙸𝙲 ‹𝟹 .")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "D_o_m_A12")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "lMl4ll")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5191100896").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/466de30ee0f9383c8e09e.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/d70bb6fa92728763c671f.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/46fa55b49b85c084159ce.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/a282c460a7f98aedbe956.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/8fe190a2a52986bd29dc5.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
