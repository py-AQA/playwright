import os
from dotenv import load_dotenv
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

# load_dotenv()
api_id = 27201409
api_hash = "986679f28924529ff90a29e788ca5d66"

# Ваши API ID и Hash аккаунт берутся из .env
# api_id = os.getenv('TELEGRAM_APP_ID')
# api_hash = os.getenv('TELEGRAM_APP_HASH')

# Используется функция StringSession из Telethon
# чтобы сохранять сессию не в DB, а ввиде текста 
#

# client = TelegramClient(StringSession(), api_id, api_hash)


with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("Your session string is:", client.session.save())

# async def main():
#     # Выводим в консоль данные о текущем пользователе, для проверки
#     me = await client.get_me()
#     print(me.stringify())
#
#     # Сюда в дальнейшем добавим вызов метода отправки сообщений
#
#     # Бот будет запущен пока мы сами не завершим его работу
#     await client.run_until_disconnected()
#
#
# if __name__ == '__main__':
#     with client:
#         client.loop.run_until_complete(main())

