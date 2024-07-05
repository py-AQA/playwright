import os
from dotenv import load_dotenv
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

load_dotenv()

# Ваши API ID и Hash аккаунт берутся из .env
api_id = os.getenv('TELEGRAM_APP_ID')
api_hash = os.getenv('TELEGRAM_APP_HASH')

# Используется функция StringSession из Telethon
# чтобы сохранять сессию не в DB, а ввиде текста 
with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("Your session string is:", client.session.save())
