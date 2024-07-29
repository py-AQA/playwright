
""" Создаем кнопку меню и список команд"""

import asyncio
import os
from typing import Final

from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv

from luma.bot.aio_bot.python_hub_studio.bot_cmd_list_les_3 import private
from luma.bot.aio_bot.python_hub_studio.handlers.user_group import user_group_router
from luma.bot.aio_bot.python_hub_studio.handlers.user_private_for_lesson_3 import user_private_router


load_dotenv()
bot_token = os.getenv("TOKEN")
BOT_USERNAME: Final = '@gromamicon_bot'
print(bot_token)

bot = Bot(bot_token)
dp = Dispatcher()
dp.include_router(user_private_router)
dp.include_router(user_group_router)

ALLOW_UPDATES = ["message, edited_message"]  # ограничивает типы апдейтов, которые к нам приходят


async def main():
    await bot.delete_webhook(drop_pending_updates=True)

    # add button of menu
    # При повторном использовании команды перечитает файл и переназначит новые кнопки меню
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())

    # delete button of menu
    # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())

    await dp.start_polling(bot, allowed_updates=ALLOW_UPDATES)

asyncio.run(main())

""" Смотри файлы в папке handlers user_private_for_lesson_3 and user_group, bot_cmd_list
создаем группу, добавляем в нее бота с правами админа, пишем в чат группы запрещенное слово  
и бот должен сделать предупреждение.
Чтобы в чате группы нельзя было пользоваться командами из меню /меню и т.д.  
Делаем фильтрацию событий в зависимости от того в каком чате событие написано.
Создаем  папку filters, в ней файл chat_types.py

В файле user_private.ру and user_group повесим проверку на роутер, чтоб проверка была до прохождения по всем хендлерам. 

В итоге в групповом чате идет фильтр по модерации, но нет возможности увидеть /команды, а в чате бота нет модерации по 
запрещенным словам
"""
