from aiogram import types, Router, F
from aiogram.filters import CommandStart

from luma.bot.aio_bot.python_hub_studio.lesson_7.filters.chat_types import ChatTypesFilter
from luma.bot.aio_bot.python_hub_studio.lesson_7.keyboards.inline import get_callback_btns

user_private_router = Router()
user_private_router.message.filter(ChatTypesFilter(['private']))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Привет, я виртуальный помощник",
                         reply_markup=get_callback_btns(btns={
                             'Нажми меня': 'some_1'
                         }))


@user_private_router.callback_query(F.data.startswith('some_'))
async def counter(callback: types.CallbackQuery):
    number = int(callback.data.split('_')[-1])

    await callback.message.edit_text(
        text=f"Нажатий - {number}",
        reply_markup=get_callback_btns(btns={
            'Нажми еще раз': f'some_{number + 1}'
        }))
#
#
# @user_private_router.message(CommandStart())
# async def start_cmd(message: types.Message):
#     await message.answer(
#         "Привет, я виртуальный помощник",
#         reply_markup=get_keyboard(
#             "Меню",
#             "О магазине",
#             "Варианты оплаты",
#             "Варианты доставки",
#             placeholder="Что вас интересует?",
#             sizes=(2, 2)
#         ),
#     )
#
#
# @user_private_router.message(F.text.lower() == "меню")
# @user_private_router.message(or_f(Command("menu"), (F.text.lower() == "меню")))
# async def menu_cmd(message: types.Message, session: AsyncSession):
#     for product in await orm_get_products(session):
#         await message.answer_photo(
#             product.image,
#             caption=f"<strong>{product.name}\
#                     </strong>\n{product.description}\nСтоимость: {round(product.price, 2)}",
#         )
#     await message.answer("Вот меню:")
#
#
# @user_private_router.message(F.text.lower() == "о магазине")
# @user_private_router.message(Command("about"))
# async def about_cmd(message: types.Message):
#     await message.answer("О нас:")
#
#
# @user_private_router.message(F.text.lower() == "варианты оплаты")
# @user_private_router.message(Command("payment"))
# async def payment_cmd(message: types.Message):
#     text = as_marked_section(
#         Bold("Варианты оплаты:"),
#         "Картой в боте",
#         "При получении карта/кеш",
#         "В заведении",
#         marker="✅ ",
#     )
#     await message.answer(text.as_html())
#
#
# @user_private_router.message(
#     (F.text.lower().contains("доставк")) | (F.text.lower() == "варианты доставки"))
# @user_private_router.message(Command("shipping"))
# async def shipping_cmd(message: types.Message):
#     text = as_list(
#         as_marked_section(
#             Bold("Варианты доставки/заказа:"),
#             "Курьер",
#             "Самовынос (сейчас прибегу заберу)",
#             "Покушаю у Вас (сейчас прибегу)",
#             marker="✅ ",
#         ),
#         as_marked_section(
#             Bold("Нельзя:"),
#             "Почта",
#             "Голуби",
#             marker="❌ "
#         ),
#         sep="\n----------------------\n",
#     )
#     await message.answer(text.as_html())
#
#
# @user_private_router.message(F.contact)
# async def get_contact(message: types.Message):
#     await message.answer(f"номер получен")
#     await message.answer(str(message.contact))
#
#
# @user_private_router.message(F.location)
# async def get_location(message: types.Message):
#     await message.answer(f"локация получена")
#     await message.answer(str(message.location))