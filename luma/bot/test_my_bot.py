import asyncio
import os
from typing import Final

import pytest
from dotenv import load_dotenv
from telethon import TelegramClient
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

client = TelegramClient(StringSession(telethon_session), int(api_id), api_hash)


@pytest.mark.asyncio
async def test_bot_say_hi():
    await client.connect()
    await client.send_message(BOT_USERNAME, '/start')
    await client.send_message(BOT_USERNAME, 'hello')
    await asyncio.sleep(2)
    async for message in client.iter_messages(BOT_USERNAME, limit=1):
        assert message.text == 'hey there'



"""  корутину можно вызвать:
await
asyncio.run()
asyncio.create_task()
loop.run_until_complete()
asyncio.gather()
asyncio.wait()
"""
