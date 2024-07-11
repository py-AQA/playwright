import os
import time

from telethon import TelegramClient
from telethon.sessions import StringSession
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv("APP_ID")
api_hash = os.getenv("APP_HASH")
telethon_session = os.getenv("SESSION_NAME")

# нужен если убрать мой конфтест файл, настройки из глобально-группового конфтеста не передаются
# def client() -> TelegramClient:
#     """Создание клиента телеграмма
#
#     :return: client connection instance
#     :rtype: TelegramClient
#     """
#     client = TelegramClient(
#         StringSession(telethon_session), api_id, api_hash
#     )
#
#     yield client


def test_bot_say_hi(client: TelegramClient):
    """ Посылаем сообщение нашему боту и проверяем что он отвечает нам """
    client = TelegramClient(StringSession(telethon_session), api_id, api_hash)
    client.connect()

    # Используется conversation из telethon для того что бы следить за диалогом с ботом
    # with client.conversation("@gromamicon_bot", timeout=5) as conv:
    client.send_message("@gromamicon_bot", "/start")
    time.sleep(1)
    resp = client.get_messages("@gromamicon_bot")
    #     resp = client._get_response_message("/start", "HI", "")
    print(resp)
    # assert resp.text == "Hi"
