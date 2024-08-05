import asyncio
import os
from typing import Final

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
from aiogram.enums import ParseMode
from luma.bot.aio_bot.python_hub_studio.bot_cmd_list_les_3 import private
from luma.bot.aio_bot.python_hub_studio.handlers.user_group import user_group_router
from luma.bot.aio_bot.python_hub_studio.handlers.user_private_4 import user_private_router

load_dotenv()
bot_token = os.getenv("TOKEN")
BOT_USERNAME: Final = '@gromamicon_bot'
print(bot_token)

bot = Bot(bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()
dp.include_router(user_private_router)
dp.include_router(user_group_router)

ALLOW_UPDATES = ["message, edited_message"]


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOW_UPDATES)


asyncio.run(main())

""" 
F.text.startswith("show") фильтр теста  - тест начинается с слова "show"
F.text.endswith("example")) - тест заканчивается  словом  "example"

and_f(F.text.startswith("show"), F.text.endswith("example")) - объединение условий  and_f

or_f(F.text(text="hi"), CommandStart()) - запуск по команде ИЛИ по тексту

@user_private_router.message(~(F.text.lower().contains ("варианты доставки")))
будет срабатывать при всех условиях, кроме "варианты доставки"
"""
