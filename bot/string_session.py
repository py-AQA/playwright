import os
from dotenv import load_dotenv
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

load_dotenv()

api_id = int(os.getenv("APP_ID"))
api_hash = os.getenv("APP_HASH")


with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("Your session string is:", client.session.save())
