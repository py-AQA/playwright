from aiogram import types, Router, F
# from luma.bot.aio_bot.python_hub_studio.lesson4.keyboards.reply_les4 import del_kbd, start_kb2
# from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, or_f
from aiogram.utils.formatting import as_list, as_marked_section, Bold
from luma.bot.aio_bot.python_hub_studio.lesson4.filters.chat_types_4 import ChatTypesFilter
# from luma.bot.aio_bot.python_hub_studio.lesson4.keyboards import reply_les4
from luma.bot.aio_bot.python_hub_studio.lesson4.keyboards.reply_les4 import start_kb3


user_private_router = Router()
user_private_router.message.filter(ChatTypesFilter(['private']))

"Функция вызова клавиатуры_1"
# @user_private_router.message(CommandStart())
# async def start_cmd(message: types.Message):
#     await message.answer(" Привет! Я ваш помощник", reply_markup=reply_les4.start_kb)


"""Функция вызова клавиатуры_2"""
# @user_private_router.message(CommandStart())
# async def start_cmd(message: types.Message):
#     await message.answer(" Привет! Я ваш помощник", reply_markup=start_kb2.as_markup(
#         resize_keyboard=True, input_field_placeholder="What do you interesting?"))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    """Функция вызова клавиатуры_3"""
    await message.answer(" Привет! Я ваш помощник", reply_markup=start_kb3.as_markup(
        resize_keyboard=True, input_field_placeholder="What do you interesting?"))


@user_private_router.message(or_f(Command("menu"), (F.text.lower() == "меню")))
# @user_private_router.message(Command("menu"))
async def menu_cmd(message: types.Message):
    await message.answer(" Вот ваше  меню")


"""
del_kbd = ReplyKeyboardRemove() -  удаляет клавиатуру

@user_private_router.message(or_f(Command("menu"), (F.text.lower() == "меню")))
# @user_private_router.message(Command("menu"))
async def menu_cmd(message: types.Message):
    await message.answer(" Вот ваше  меню", reply_markup=del_kbd)
    """


@user_private_router.message(or_f(Command("about"), (F.text.lower() == "о магазине")))
# @user_private_router.message(F.text.lower() == "о нас")
# @user_private_router.message(Command("about"))
async def about_cmd(message: types.Message):
    await message.answer("Информация о нас")


@user_private_router.message(or_f(Command("payment"), (F.text.lower().contains("оплат"))))
# @user_private_router.message(F.text.lower() == "варианты оплаты")
# @user_private_router.message(Command("payment"))
async def payment_cmd(message: types.Message):
    # await message.answer("Выбери варианты оплаты ")
    text = as_marked_section(
        Bold("Варианты оплаты:"),
        "Картой в боте",
        "При получении карта/кеш",
        "В заведении",
        marker='✅ '
    )
    await message.answer(text.as_html())


@user_private_router.message(or_f(Command("shipping"),
                                  (F.text.lower().contains("доставк")) | (F.text.lower() == "варианты доставки")))

# @user_private_router.message((F.text.lower().contains("доставк")) | (F.text.lower() == "варианты доставки"))
# @user_private_router.message(Command("shipping"))
async def shipping_cmd(message: types.Message):
    await message.answer("Выбери варианты доставки")
    #  parse_mode=ParseMode.HTML во все хендлеры ставить не красиво, укажем его в lesson4, bot
    # await message.answer("<b>Выбери варианты доставки</b>", parse_mode=ParseMode.HTML)
    text = as_list(
        as_marked_section(
            Bold("Варианты доставки/заказа:"),
            "Курьер",
            "Самовынос (сейчас прибегу заберу)",
            "Покушаю у Вас (сейчас прибегу)",
            marker='✅ '
        ),
        as_marked_section(
            Bold("Нельзя:"),
            "Почта",
            "Голуби",
            marker='❌ '
        ),
        sep='\n----------------------\n'
    )
    await message.answer(text.as_html())





@user_private_router.message(F.contact)
async def get_contact(message: types.Message):
    await message.answer(f"номер получен")
    await message.answer(str(message.contact))
#  в объекте contact будет находиться вся информация
#  после contact ставим точку и смотрим информацию (номер телефона,ФИО и т.д.)


@user_private_router.message(F.location)
async def get_location(message: types.Message):
    await message.answer(f"локация получена")
    await message.answer(str(message.location))
#  в объекте location будет находиться вся информация
#  после contact ставим точку и смотрим информацию (Долгота, широта и т.д.)

# (F.text) хендлер попадет в любое сообщение от пользователя, если оно текст.
# Ставим его ниже всех, улавливает все смс, даже команды







"""


(()F.text.lower().contains("доставк")) | (F.text.lower() == "варианты доставки")) условия записаны как "ИЛИ"
((F.text.lower().contains("доставк")) & (F.text.lower() == "варианты доставки"))  условия записаны как "И"

@user_private_router.message(~(F.text.lower().contains ("варианты доставки")))
будет срабатывать при всех условиях, кроме "варианты доставки"

#  parse_mode=ParseMode.HTML во все хендлеры ставить не красиво, укажем его в lesson4, bot
# await message.answer("<b>Выбери варианты доставки</b>", parse_mode=ParseMode.HTML)

#  в объекте location будет находиться вся информация
#  после contact ставим точку и смотрим информацию (Долгота, широта и т.д.)

#  в объекте contact будет находиться вся информация
#  после contact ставим точку и смотрим информацию (номер телефона,ФИО и т.д.)

"""
