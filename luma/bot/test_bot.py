import asyncio
import os
from typing import Final

import pytest
from dotenv import load_dotenv
from telethon import TelegramClient
# from telethon.sync import TelegramClient
from telethon.sessions import StringSession

load_dotenv()

bot_token = os.getenv("TOKEN")
api_id = os.getenv("APP_ID")
api_hash = os.getenv("APP_HASH")
telethon_session = os.getenv("SESSION_NAME")
BOT_USERNAME: Final = '@gromamicon_bot'
print(telethon_session)
print(api_id)
print(api_hash)
#
# client = TelegramClient(StringSession(telethon_session), int(api_id), api_hash)


@pytest.fixture
def client_fixture():
    # Создайте и верните объект TelegramClient
    client = TelegramClient(StringSession(telethon_session), int(api_id), api_hash)
    return client


@pytest.mark.asyncio
async def test_bot_echo(client_fixture):
    client = client_fixture
    async with client:
        await client.connect()
        await client.send_message(BOT_USERNAME, '/start')
        await client.send_message(BOT_USERNAME, '/caps')
        await client.send_message(BOT_USERNAME, 'hello')
        await asyncio.sleep(2)
        async for message in client.iter_messages(BOT_USERNAME, limit=1):
            assert message.text == 'hey there' or message.text == "HEY THERE"

    loop = asyncio.get_event_loop()
    if not loop.is_running():
        loop.run_until_complete(asyncio.gather(
            test_inline_key_button(client_fixture)
        ))


@pytest.mark.asyncio
@pytest.mark.parametrize("button, expect", [(b'place_info', "Несмотря на"),
                                            (b'visit', ""), (b'contact_info', "Служба Поддержки")],
                         ids=["place_info", "visit", "contact_info"])
async def test_inline_key_button(client_fixture, button, expect):
    client = client_fixture
    await client.connect()
    await client.send_message(BOT_USERNAME, '/start')
    client.list_event_handlers()
    await asyncio.sleep(1)

    async for message in client.iter_messages(BOT_USERNAME, limit=1):
        print(message.reply_markup)
        print(message.reply_markup.rows[0].buttons[0].data)
        print(message.reply_markup.rows[1].buttons[0].data)
        print(message.reply_markup.rows[2].buttons[0].data)

        # await message.buttons[0][0].click()
        await message.click(data=button)

        await asyncio.sleep(1)
    async for message in client.iter_messages(BOT_USERNAME, limit=1):
        assert message.text.startswith(expect)

    await asyncio.sleep(4)

    loop = asyncio.get_event_loop()
    if not loop.is_running():
        loop.run_until_complete(asyncio.gather(
            test_inline_key_button(client_fixture, button, expect)
        ))
"""Добавив этот блок кода, цикл событий будет ожидать завершения всех асинхронных операций, включая выполнение ваших 
тестов, прежде чем он будет закрыт. Это поможет избежать ошибки, связанной с закрытием цикла событий до завершения 
всех необходимых операций."""


@pytest.mark.asyncio
async def test_inline_key_button2(client_fixture):
    client = client_fixture
    async with client:
        await client.connect()
        await client.send_message(BOT_USERNAME, '/start')
        client.list_event_handlers()
        await asyncio.sleep(2)

        async for message in client.iter_messages(BOT_USERNAME, limit=1):
            print(message.reply_markup)
            print(message.reply_markup.rows[0].buttons[0].data)
            print(message.reply_markup.rows[1].buttons[0].data)
            print(message.reply_markup.rows[2].buttons[0].data)

            # await message.buttons[0][0].click()
            await message.click(data=b'place_info')

            await asyncio.sleep(1)
        async for message in client.iter_messages(BOT_USERNAME, limit=1):
            assert message.text.startswith("Несмотря на ")

            await asyncio.sleep(1)
            await message.click(data=b'visit')

            await asyncio.sleep(1)
            assert message.text.startswith("")

            await asyncio.sleep(2)
            await message.click(data=b'contact_info')
            assert message.text.startswith("Служба Поддержки")

    loop = asyncio.get_event_loop()
    if not loop.is_running():
        loop.run_until_complete(asyncio.gather(test_inline_key_button2()))


    # print(message)

    # async for message in client.iter_messages(BOT_USERNAME, limit=1):

    # await message.click(data=b'contact_info')

    # await asyncio.sleep(1)
    # async for message in client.iter_messages(BOT_USERNAME, limit=3):
    #     print(message.reply_markup)
    #     print(message.reply_markup)
    #     await message.click(data=b'contact_info')
    # await message.buttons[2][0].click()

    # print(Message.buttons)

    # client(GetBotCallbackAnswerRequest(BOT_USERNAME, message.id, data=message.reply_markup.rows[0].buttons[0].data))

    """messages[0].reply_markup.rows[0].buttons[0].data
GetBotCallbackAnswerRequest is what "presses" or "interacts" the buttons, and you linked to the right place indeed. 
What's your issue exactly? With messages[0].reply_markup.rows[0].buttons[0].data you access the data, with the linked:
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest

client(GetBotCallbackAnswerRequest(
    user_or_chat,
    msg.id,
    data=msg.reply_markup.rows[wanted_row].buttons[wanted_button].data
))"""




"""  корутину можно вызвать:
await
asyncio.run()
asyncio.create_task()
loop.run_until_complete()
asyncio.gather()
asyncio.wait()
"""
