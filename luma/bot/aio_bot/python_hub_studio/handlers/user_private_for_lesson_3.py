from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from luma.bot.aio_bot.python_hub_studio.filters.chat_types import ChatTypesFilter


user_private_router = Router()
user_private_router.message.filter(ChatTypesFilter(['private']))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Welcome to the bot!")


@user_private_router.message(Command("menu"))
async def menu_cmd(message: types.Message):
    await message.answer(" Menu")


@user_private_router.message(Command("about"))
async def about_cmd(message: types.Message):
    await message.answer(" about us")


@user_private_router.message(Command("payment"))
async def payment_cmd(message: types.Message):
    await message.answer("payment options")


@user_private_router.message(Command("shipping"))
async def shipping_cmd(message: types.Message):
    await message.answer("delivery options")


# (F.text) хендлер попадет в любое сообщение от пользователя, если оно текст.
# Ставим его ниже всех, улавливает все смс, даже команды
@user_private_router.message(F.text.lower() == "magic")
async def f_cmd(message: types.Message):
    await message.answer("This is  magic filter")
