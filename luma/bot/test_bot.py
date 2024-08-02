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


@pytest.fixture
def client():
    client = TelegramClient(StringSession(telethon_session), int(api_id), api_hash)
    return client


@pytest.mark.asyncio
async def test_bot_echo(client):
    async with client:
        await client.connect()
        await client.send_message(BOT_USERNAME, '/start')
        await asyncio.sleep(1)
        await client.send_message(BOT_USERNAME, '/caps')
        await asyncio.sleep(1)
        await client.send_message(BOT_USERNAME, 'hello')
        await asyncio.sleep(1)
        async for message in client.iter_messages(BOT_USERNAME, limit=1):
            assert message.text == 'hey there' or message.text == "HEY THERE"

    loop = asyncio.get_event_loop()
    if not loop.is_running():
        loop.run_until_complete(asyncio.gather(
            test_inline_key_button(client)
        ))


@pytest.mark.asyncio
@pytest.mark.parametrize("button, expect", [(b'place_info', "Несмотря на"),
                                            (b'visit', ""), (b'contact_info', "Служба Поддержки")],
                         ids=["place_info", "visit", "contact_info"])
async def test_inline_key_button(client, button, expect):
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
            test_inline_key_button(client, button, expect)
        ))

"""Добавив этот блок кода, (loop =) цикл событий будет ожидать завершения всех асинхронных операций, включая выполнение ваших 
тестов, прежде чем он будет закрыт. Это поможет избежать ошибки, связанной с закрытием цикла событий до завершения 
всех необходимых операций."""


@pytest.mark.asyncio
async def test_inline_key_button_menu(client):
    async with client:
        await client.connect()
        await client.send_message(BOT_USERNAME, '/start')
        client.list_event_handlers()
        await asyncio.sleep(2)

        async for message in client.iter_messages(BOT_USERNAME, limit=1):
            """Получаем список событий и фильтруем- показать последнюю строку.
            data=b'place_info' - первый вариант адресов кнопок.
            Ниже второй вариант записи адреса кнопок:
            ряд -rows[0] и  номер кнопки по индексу [0] , в данном случае - 1 ряд и  первая кнопка """

            print(message.reply_markup)
            print(message.reply_markup.rows[0].buttons[0].data)
            print(message.reply_markup.rows[1].buttons[0].data)
            print(message.reply_markup.rows[2].buttons[0].data)

            # await message.buttons[0][0].click()
            await message.click(data=b'place_info')

            await asyncio.sleep(1)
        async for message in client.iter_messages(BOT_USERNAME, limit=1):
            "Сравниваем тест ответа бота, после клика кнопки на частичное совпадение"
            assert message.text.startswith("Несмотря на ")

        await asyncio.sleep(1)
        async for message in client.iter_messages(BOT_USERNAME, limit=1, offset_id=106850):
            """ Смотрим в список событий , ищем нужный message_id  с помощью строки 
             async for message in client.iter_messages(BOT_USERNAME, limit=2):
               print(message)
             limit=2  нужен чтобы увидеть не текстовое смс после клика,  а строку с списком кнопок, 
             которая уже предпоследняя в списке событий. 
             Добавляем к нужному  message_id  +1 и пишем  в offset_id= наш результат.
             
             С помощью этой записи  получаем список кнопок с их именами:
             async for message in client.iter_messages(BOT_USERNAME, limit=1, offset_id=106850):
              print(message.reply_markup)
             """

            print(message)
            await message.click(data=b'visit')
            assert message.text.startswith("")

            await message.click(data=b'contact_info')
            await asyncio.sleep(1)
        async for message in client.iter_messages(BOT_USERNAME, limit=1):
            "Получаем последнее событие после клика - сообщение после клика"
            assert message.text.startswith("Служба Поддержки")

    loop = asyncio.get_event_loop()
    if not loop.is_running():
        loop.run_until_complete(asyncio.gather(test_inline_key_button_menu()))


@pytest.mark.asyncio
async def test_inline_key_button_description(client):
    async with client:
        await client.connect()
        await client.send_message(BOT_USERNAME, '/start')
        client.list_event_handlers()
        await asyncio.sleep(2)

        async for message in client.iter_messages(BOT_USERNAME, limit=1, offset_id=106947):
            print(message)
            assert message.text.startswith("Hi! Do you like this picture?")
            print(message.reply_markup)
            print(message.reply_markup.rows[0].buttons[0].data)
            print(message.reply_markup.rows[0].buttons[1].data)

            await message.click(data=b'like')
            await asyncio.sleep(1)
        async for message in client.iter_messages(BOT_USERNAME, limit=1):
            assert message.text.startswith("You like this photo")

        async for message in client.iter_messages(BOT_USERNAME, limit=1, offset_id=106947):
            await asyncio.sleep(1)
            await message.click(data=b'dislike')

            await asyncio.sleep(1)
        async for message in client.iter_messages(BOT_USERNAME, limit=1):
            assert message.text.startswith("You dont like this photo")

    loop = asyncio.get_event_loop()
    if not loop.is_running():
        loop.run_until_complete(asyncio.gather(test_inline_key_button_menu()))

    """  Карутину можно вызвать:
    await
    asyncio.run()
    asyncio.create_task()
    loop.run_until_complete()
    asyncio.gather()
    asyncio.wait()
    """

    """messages[0].reply_markup.rows[0].buttons[0].data
GetBotCallbackAnswerRequest is what "presses" or "interacts" the buttons, and you linked to the right place indeed. 
What's your issue exactly? With messages[0].reply_markup.rows[0].buttons[0].data you access the data, with the linked:
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest

client(GetBotCallbackAnswerRequest(user_or_chat, msg.id, 
data=msg.reply_markup.rows[wanted_row].buttons[wanted_button].data) """

# client(GetBotCallbackAnswerRequest(BOT_USERNAME, message.id, data=message.reply_markup.rows[0].buttons[0].data))


