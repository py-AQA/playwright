import asyncio
import os
import time

import pytest
from dotenv import load_dotenv
from pytest import mark
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.custom.message import Message

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
#         StringSession(telethon_session), int(api_id), api_hash
#     )
#
#     yield client


def test_bot_say_hi(client: TelegramClient):
    """ Посылаем сообщение нашему боту и проверяем что он отвечает нам """
    client = TelegramClient(StringSession(telethon_session), int(api_id), api_hash)
    client.connect()

    # Используется conversation из telethon для того что бы следить за диалогом с ботом
    # with client.conversation("@gromamicon_bot", timeout=5) as conv:
    client.send_message("@gromamicon_bot", "/start")
    # time.sleep(1)
    # resp = client.get_messages("@gromamicon_bot")
    # #     resp = client._get_response_message("/start", "HI", "")
    # print(resp)
    # assert resp.text == "Hi"


@mark.asyncio
async def test_bot_send_message(client: TelegramClient):
    with client.conversation("@gromamicon_bot", timeout=5) as conv:
        await client.connect()
        await conv.send_message("/start")
        resp: Message = await conv.get_response()
        # resp = await conv.get_response()
        print(resp)
        # assert resp.text == "Hi"




