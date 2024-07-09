import pytest
from telethon import TelegramClient


@pytest.mark.asyncio
async def test_bot_say_hi(client: TelegramClient):
    """ Посылаем сообщение нашему боту и проверяем что он отвечает нам """

    # Вызывает ошибку event_loop если делать connect() в fixture, пока решено оставить здесь
    await client.connect()

    # Используется conversation из telethon для того что бы следить за диалогом с ботом
    async with client.conversation("@gromamicon_bot", timeout=5) as conv:
        await conv.send_message("/start")
        resp = await conv.get_response()

        assert resp.text == "Hi"

    