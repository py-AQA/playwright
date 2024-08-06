from aiogram import types, Router
from aiogram.filters import CommandStart, Command

user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message) -> None:
    await message.answer("Welcome to the bot!")


@user_private_router.message(Command("menu"))
async def menu(message: types.Message) -> None:
    await message.answer(" Menu")


# @dp.message() перехватывает все смс, должно быть после команды старт
@user_private_router.message()
async def echo(message: types.Message) -> None:
    text: str | None = message.text

    if text in ["Hi", "hi", "Hello", "hello"]:
        await  message.answer("Hi and you")
    elif text in ["bye", "good bye"]:
        await message.answer("bye")
    else:
        await message.answer(message.text)
        #  message.answer отправляется тому же самому пользователю и в ту же самую группу
        await message.reply(message.text)
        #  message.reply отправляется с упоминанием автора смс, на которое отвечаем
