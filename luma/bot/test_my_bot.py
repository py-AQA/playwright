import asyncio
import os
from typing import Final

import pytest
from dotenv import load_dotenv
from pytest import mark
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.custom import Conversation
from telethon.tl.custom.message import Message

load_dotenv()

bot_token = os.getenv("TOKEN")
api_id = os.getenv("APP_ID")
api_hash = os.getenv("APP_HASH")
telethon_session = os.getenv("SESSION_NAME")
BOT_USERNAME: Final = '@gromamicon_bot'
print(telethon_session)
print(api_id)
print(api_hash)


# my_client = TelegramClient(StringSession(telethon_session), int(api_id), api_hash)


@pytest.mark.asyncio
@pytest.fixture(scope="session", autouse=True)
def client() -> TelegramClient:
    client = TelegramClient(StringSession(telethon_session), int(api_id), api_hash)
    # client.connect()
    # client.get_me()
    # client.get_dialogs()
    # try:
    return client
    # finally:
    #     client.disconnect()

# @pytest.mark.asyncio
# @pytest.fixture(scope="session")
# async def client() -> TelegramClient:
#     client = TelegramClient(
#         StringSession(telethon_session), int(api_id), api_hash,
#         sequential_updates=True
#     )
#     # Connect to the server
#     await client.connect()
#     # Issue a high level command to start receiving message
#     await client.get_me()
#     # Fill the entity cache
#     await client.get_dialogs()
#
#     yield client
#
#     await client.disconnect()
#     await client.disconnected


@pytest.fixture(scope="session")
async def conv(client: TelegramClient):
    async with client.conversation(BOT_USERNAME, timeout=10, max_messages=10000) as conversation:
        await conversation.connect()
        await conversation.send_message("/start")
        await conversation.get_response()
        yield conversation


@pytest.mark.asyncio
async def test_bot_say_hi(client):
    # async with client.conversation(BOT_USERNAME, timeout=5) as conv:
    conv = client.conversation(BOT_USERNAME, timeout=5)
    await conv.send_message('Hello!')
    print(conv)
    message = await conv.get_response()
    await conv.get_reply()

    assert message.text == 'hey there'


@mark.asyncio
async def test_help(client: TelegramClient):
    # Create a conversation
    with client.conversation(BOT_USERNAME, timeout=5) as conv:
        # Send a command
        await conv.send_message("/help")
        # Get response
        resp: Message = await conv.get_response()
        # Make assertions
        assert BOT_USERNAME in resp.raw_text
        assert "👍" in resp.raw_text
        assert "👎" in resp.raw_text










@pytest.mark.asyncio
async def test_bot_say_hi_2(client):
    await client.connect()
    await client.send_message(BOT_USERNAME, '/start')
    await client.send_message(BOT_USERNAME, 'hello')
    await asyncio.sleep(2)
    async for message in client.iter_messages(BOT_USERNAME, limit=1):
        assert message.text == 'hey there'


@pytest.mark.asyncio
@pytest.mark.parametrize("button", [b'place_info', b'visit', b'contact_info'])
async def test_inline_key_button(client: TelegramClient, button):
    # await client.connect()

    async with client.conversation(
            BOT_USERNAME, timeout=10, max_messages=10000
    ) as conv:
        conv: Conversation

    await conv.send_message(BOT_USERNAME, '/start')
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
        assert message.text.startswith("Несмотря на ")

    await asyncio.sleep(10)

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

    # message_type: str = message.chat.type
    # text: str = message.text
    # processed: str = text.lower()
    # print(f'User({message.chat.id}) in {message_type}: "{text}"')
    # print(client)
    # query = update.callback_query
    # button = query.data


"""  корутину можно вызвать:
await
asyncio.run()
asyncio.create_task()
loop.run_until_complete()
asyncio.gather()
asyncio.wait()
"""
