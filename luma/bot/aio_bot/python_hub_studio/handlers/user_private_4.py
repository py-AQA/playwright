from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f
from luma.bot.aio_bot.python_hub_studio.filters.chat_types import ChatTypesFilter
from luma.bot.aio_bot.python_hub_studio.keyboards import reply_les4

user_private_router = Router()
user_private_router.message.filter(ChatTypesFilter(['private']))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(" Привет! Я ваш помощник", reply_markup=reply_les4.start_kb)


@user_private_router.message(or_f(Command("menu"), (F.text.lower() == "меню")))
# @user_private_router.message(Command("menu"))
async def menu_cmd(message: types.Message):
    await message.answer(" Вот ваше  меню")


@user_private_router.message(F.text.lower() == "о нас")
# @user_private_router.message(Command("about"))
async def about_cmd(message: types.Message):
    await message.answer("Информация о нас")


@user_private_router.message(F.text.lower() == "варианты оплаты")
# @user_private_router.message(Command("payment"))
async def payment_cmd(message: types.Message):
    await message.answer("Варианты оплаты ")


@user_private_router.message(F.text.lower().contains("доставк")) | (F.text.lower() == "варианты доставки")
# @user_private_router.message(Command("shipping"))
async def shipping_cmd(message: types.Message):
    await message.answer("Варианты доставки")


# (F.text) хендлер попадет в любое сообщение от пользователя, если оно текст.
# Ставим его ниже всех, улавливает все смс, даже команды
@user_private_router.message(F.text.lower() == "magic")
async def f_cmd(message: types.Message):
    await message.answer("This is  magic filter")
