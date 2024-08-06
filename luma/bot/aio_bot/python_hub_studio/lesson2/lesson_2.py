import asyncio
import os
from typing import Final

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from luma.bot.aio_bot.python_hub_studio.lesson2.user_private_2 import user_private_router

load_dotenv()
bot_token = os.getenv("TOKEN")
BOT_USERNAME: Final = '@gromamicon_bot'
print(bot_token)

bot = Bot(bot_token)
dp = Dispatcher()  # Главный роутер
dp.include_router(user_private_router)

ALLOW_UPDATES = ["message, edited_message"]  # ограничивает типы апдейтов, которые к нам приходят

" Переносим функцию в user_privat.py, поэтому закоментирована"
# @dp.message(CommandStart())
# async def start_cmd(message: types.Message) -> None:
#     await message.answer("Welcome to the bot!")


" Переносим функцию в user_privat.py, поэтому закоментирована"
# @dp.message()
# async def echo(message: types.Message) -> None:
#     text: str | None = message.text
#
#     if text in ["Hi", "hi", "Hello", "hello"]:
#         await  message.answer("Hi and you")
#     elif text in ["bye", "good bye"]:
#         await message.answer("bye")
#     else:
#         await message.answer(message.text)
#         await message.reply(message.text)


async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    # bot.delete_webhook() в идеале используется, когда бот на реальном сервере
    # drop_pending_updates=True сброс ожидающих ответа смс, когда бот был офлайн.
    # Обработка смс ботом начнется с момента нахождения бота онлайн
    await dp.start_polling(bot, allowed_updates=ALLOW_UPDATES)

asyncio.run(main())

"""Создаем структуру проекта:
создаем папку handlers 
создаем  файлы admin_privat.py and user_privat.py
переносим  @dp.message(CommandStart()) и @dp.message() в user_private.py
"""
