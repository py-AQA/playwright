import os

from dotenv import load_dotenv
from telethon.sessions import StringSession
from telethon.sync import TelegramClient

load_dotenv()
api_id = os.getenv('APP_ID')
api_hash = os.getenv('APP_HASH')
session = os.getenv("SESSION_NAME")

with TelegramClient(StringSession(session), api_id, api_hash) as client:
    print("Your session string is:", client.session.save())
    print(client.get_me())


async def main():
    # Выводим в консоль данные о текущем пользователе, для проверки
    me = await client.get_me()
    print(me.stringify())
