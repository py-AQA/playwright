
"""========   Асинхронная SqlAlchemy | База Данных в Telegram боте  ==============="""
import asyncio
import os
from typing import Final

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import find_dotenv, load_dotenv

from bot_cmd_list import private
from handlers.user_group import user_group_router
from handlers.user_private import user_private_router
from luma.bot.aio_bot.python_hub_studio.lesson_6.database.engine import create_db, drop_db, session_maker
from luma.bot.aio_bot.python_hub_studio.lesson_6.handlers.admin_private import admin_router
from luma.bot.aio_bot.python_hub_studio.lesson_6.middlewares.db import DataBaseSession
# from middlewares.db import CounterMiddleware, CounterMiddleware2

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

# Регистрируем наш слой .middleware он работает после фильтров, вешаем его на роутер
# admin_router.message.outer_middleware работает перед фильтрами
# порядок строк имеет значение admin_router.message.middleware должен быть после dp.include_router(admin_router)

# admin_router.message.middleware(CounterMiddleware())  # "обрабатывает Message"
# admin_router.message.middleware(CounterMiddleware2())  # "обрабатывает TelegramObject"

"""  запись  Вариант 2. 
Вешаем слой на Dispatcher()
У Dispatcher() есть глобальное событие update
dp.update.outer_middleware(CounterMiddleware()) - этот промежуточный слой срабатывает раньше всех 
"""


# ALLOWED_UPDATES = ['message', 'edited_message', 'callback_query']
# Чтоб не передавать  список ALLOWED_UPDATES  вручную, можно  указать
# dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


async def on_startup(bot):
    run_param = False
    if run_param:
        await drop_db()

    await create_db()

""" Если run_param будет True, сбросить все таблицы перед запуском, потом создать новые .
Если таблица существует, функция ничего не делает    """


async def on_shutdown(bot):
    print('бот лег')


async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    # Вешаем на update после прохождения всех фильтров
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

""" 
pip install sqlalchemy
pip install aiosqlite
pip install asyncpg    - установка PostgreSQL

pip install aiomysql - MySQl

pip install mysql-connector-python   библиотека для не асинхронной работы

"""
