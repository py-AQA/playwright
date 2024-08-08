import asyncio
import os
from typing import Final

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv, find_dotenv

from bot_cmd_list_5 import private
from handlers.user_group_5 import user_group_router
from handlers.user_private_5 import user_private_router
from luma.bot.aio_bot.python_hub_studio.lesson5.handlers.admin_private import admin_router

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

ALLOW_UPDATES = ["message, edited_message"]


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOW_UPDATES)


if __name__ == '__main__':
    try:
        asyncio.set_event_loop(asyncio.new_event_loop())
        asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        print("Program was interrupted by the user.")


""" 
F.text.startswith("show") фильтр теста  - тест начинается с слова "show"
F.text.endswith("example")) - тест заканчивается  словом  "example"

and_f(F.text.startswith("show"), F.text.endswith("example")) - объединение условий  and_f

or_f(F.text(text="hi"), CommandStart()) - запуск по команде ИЛИ по тексту

@user_private_router.message(~(F.text.lower().contains ("варианты доставки")))
будет срабатывать при всех условиях, кроме "варианты доставки"

Блок:
if __name__ == '__main__':
    try:
        asyncio.set_event_loop(asyncio.new_event_loop()) ...........
        Добавлен, чтоб исключить ошибку при остановке программы вручную
  

"""
