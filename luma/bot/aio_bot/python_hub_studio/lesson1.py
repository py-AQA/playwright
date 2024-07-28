import os
from typing import Final
import asyncio
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from aiogram.filters import CommandStart

load_dotenv()
bot_token = os.getenv("TOKEN")
BOT_USERNAME: Final = '@gromamicon_bot'
print(bot_token)

bot = Bot(bot_token)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message) -> None:
    await message.answer("Welcome to the bot!")


# @dp.message() перехватывает все смс, должно быть после команды старт
@dp.message()
async def echo(message: types.Message) -> None:
    text: str | None = message.text

    if text in ["Hi", "hi", "Hello", "hello"]:
        await  message.answer("Hi and you")
    elif text in ["bye", "good bye"]:
        await message.answer("bye")
    else:
        await message.answer(message.text)


async def main() -> None:
    await dp.start_polling(bot)

asyncio.run(main())
