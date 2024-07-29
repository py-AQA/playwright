import asyncio
import os
from typing import Final

import pytest
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.sessions import StringSession
from telegram import Update, Message
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest


load_dotenv()

bot_token = os.getenv("TOKEN")
api_id = os.getenv("APP_ID")
api_hash = os.getenv("APP_HASH")
telethon_session = os.getenv("SESSION_NAME")
BOT_USERNAME: Final = '@gromamicon_bot'
print(telethon_session)
print(api_id)
print(api_hash)

client = TelegramClient(StringSession(telethon_session), int(api_id), api_hash)


@pytest.mark.asyncio
async def test_bot_say_hi():
    await client.connect()
    await client.send_message(BOT_USERNAME, '/start')
    await client.send_message(BOT_USERNAME, 'hello')
    await asyncio.sleep(2)
    async for message in client.iter_messages(BOT_USERNAME, limit=1):
        assert message.text == 'hey there'


@pytest.mark.asyncio
async def test_inline_key_button():
    await client.connect()

    await client.send_message(BOT_USERNAME, '/start')
    client.list_event_handlers()
    await asyncio.sleep(2)

    message: Message
    # print(message)

    async for message in client.iter_messages(BOT_USERNAME, limit=1):
        print(message.reply_markup)

        print(message.reply_markup.rows[0].buttons[0].data)

        # await message.buttons[0][0].click()
        await message.click(data=b'place_info')

    await asyncio.sleep(2)
    async for message in client.iter_messages(BOT_USERNAME, limit=1):
        assert message.text.startswith("Несмотря на ")



        # await message.click(data=b'visit')


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
