#@Courselelohelp_bot
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "23664819"))
API_HASH = environ.get("API_HASH", "3853f97c662d5d08cee5f0d07361361e")
BOT_TOKEN = environ.get("BOT_TOKEN", "7694651611:AAFj-XVfUmXbZGK690521MdOlEdg8RygLvs")
OWNER = int(environ.get("OWNER", "8004315740"))
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
