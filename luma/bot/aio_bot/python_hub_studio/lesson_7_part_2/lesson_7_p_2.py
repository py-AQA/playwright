
"""" ===================Многоуровневое инлайн меню, каталог, пагинация, корзина
 https://www.youtube.com/watch?v=qfNRbyvx5Uo&list=PLNi5HdK6QEmWLtb8gh8pwcFUJCAabqZh_&index=10  ===================="""

import asyncio
import os
from typing import Final

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import find_dotenv, load_dotenv

from luma.bot.aio_bot.python_hub_studio.lesson_7_part_2.general.bot_cmd_list import private
from luma.bot.aio_bot.python_hub_studio.lesson_7_part_2.handlers.user_group import user_group_router
from luma.bot.aio_bot.python_hub_studio.lesson_7_part_2.handlers.user_private import user_private_router
from luma.bot.aio_bot.python_hub_studio.lesson_7_part_2.handlers.admin_private import admin_router

from luma.bot.aio_bot.python_hub_studio.lesson_7_part_2.database.engine import create_db, session_maker, drop_db
from luma.bot.aio_bot.python_hub_studio.lesson_7_part_2.middlewares.db import DataBaseSession


load_dotenv(find_dotenv())
bot_token = os.getenv("TOKEN")
BOT_USERNAME: Final = '@gromamicon_bot'
print(bot_token)

bot = Bot(bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
bot.my_admins_list = []
print(bot.my_admins_list)

dp = Dispatcher()

dp.include_router(user_private_router)
dp.include_router(user_group_router)
dp.include_router(admin_router)


async def on_startup(bot):
    # await drop_db()

    await create_db()


async def on_shutdown(bot):
    print('бот лег')


async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    dp.update.middleware(DataBaseSession(session_pool=session_maker))

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    try:
        asyncio.set_event_loop(asyncio.new_event_loop())
        asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        print("Program was interrupted by the user.")

# asyncio.run(main())


""" 
pip install sqlalchemy
pip install aiosqlite
pip install aiomysql - MySQl

# ALLOWED_UPDATES = ['message', 'edited_message', 'callback_query']
# Чтоб не передавать  список ALLOWED_UPDATES  вручную, можно  указать
# dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

Если run_param будет True, сбросить все таблицы перед запуском, потом создать новые .
Если таблица существует, функция ничего не делает  
"""
