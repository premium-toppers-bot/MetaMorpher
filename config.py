#ALL FILES UPLOADED - CREDITS 🌟 - @SuperToppers
import re
from os import environ
import os

id_pattern = re.compile(r'^.\d+$')


API_ID = os.environ.get("API_ID", "22182189")
API_HASH = os.environ.get("API_HASH", "5e7c4088f8e23d0ab61e29ae11960bf5")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", '8181241262'))
FSUB_UPDATES = os.environ.get("FSUB_CHANNEL", "SuperToppersChannel")
FSUB_GROUP = os.environ.get("FSUB_GROUP", "SuperToppers")
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://sujoy123m:wTWKGUaxYE7dxb1l@cluster0.zorxb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
CAPTION = os.environ.get("CAPTION", "Join @SuperToppers For More...")
group = environ.get('GROUP', '-1002101492616')
GROUP = int(group) if group and id_pattern.search(group) else None
#ALL FILES UPLOADED - CREDITS 🌟 - @SuperToppers
SUNRISES_PIC= "https://ibb.co/rGGbmNv5"  # Replace with your Telegraph link
AUTH_USERS = int(os.environ.get("AUTH_USERS", '7955112452'))
WEBHOOK = bool(os.environ.get("WEBHOOK", True))
PORT = int(os.environ.get("PORT", "8080"))
LOG_CHANNEL_ID = os.environ.get("LOG_CHANNEL_ID", -1002337242559)
