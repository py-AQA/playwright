import asyncio
import os
from typing import Final

import pytest
import pytest_asyncio
from dotenv import load_dotenv
from pytest import mark
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.custom.message import Message

from luma.bot.conftest import client

load_dotenv()

api_id = os.getenv("APP_ID")
api_hash = os.getenv("APP_HASH")
telethon_session = os.getenv("SESSION_NAME")
BOT_USERNAME: Final = '@gromamicon_bot'
print(telethon_session)
print(api_id)
print(api_hash)


# def test_bot_say_hi(client: TelegramClient):
#     """ Посылаем сообщение нашему боту и проверяем что он отвечает нам """
# client = TelegramClient(StringSession(telethon_session), int(api_id), api_hash)
# client.connect()

# Используется conversation из telethon для того что бы следить за диалогом с ботом
# with client.conversation("@gromamicon_bot", timeout=5) as conv:
# client.send_message("@gromamicon_bot", "/start")
# time.sleep(1)
# resp = client.get_messages("@gromamicon_bot")
# #     resp = client._get_response_message("/start", "HI", "")
# print(resp)
# assert resp.text == "Hi"


@mark.asyncio
async def test_bot_send_message(client):
    async with client.conversation(BOT_USERNAME, timeout=5) as conv:
        conv.send_message(BOT_USERNAME, "/start")
        resp = await conv.get_response()
        print(resp)

    asyncio.run(test_bot_send_message())


async def clients():
    client1 = TelegramClient(
        StringSession(telethon_session), int(api_id), api_hash,
        sequential_updates=True
    )

    await client1.connect()
    await client1.get_me()
    await client1.get_dialogs()
    await client1.disconnect()


async def send_messages():
    client1 = TelegramClient(
        StringSession(telethon_session), int(api_id), api_hash,
        sequential_updates=True
    )

    await client1.connect()
    await client1.get_me()
    await client1.get_dialogs()
    await client1.send_message(BOT_USERNAME, "/start")
    resp = await client1.get_messages(BOT_USERNAME)
    # resp = client1._get_response_message("/start", "Hello! Thank you for chatting with me!", "")
    print(resp)

    await client1.disconnect()


async def test_main():
    task_1 = asyncio.create_task(clients())
    task_2 = asyncio.create_task(send_messages())

    await task_1
    await task_2

asyncio.run(test_main())



# if __name__ == '__main__':
#     asyncio.run(main())


"""  корутину можно вызвать:
await
asyncio.run()
asyncio.create_task()
loop.run_until_complete()
asyncio.gather()
asyncio.wait()
"""
