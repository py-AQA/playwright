""" https://www.youtube.com/watch?v=qfNRbyvx5Uo&list=PLNi5HdK6QEmWLtb8gh8pwcFUJCAabqZh_&index=8"""

from aiogram import types, Router, F
from aiogram.filters import CommandStart
from sqlalchemy.ext.asyncio import AsyncSession

from luma.bot.aio_bot.python_hub_studio.lesson_7_part_2.database.orm_query import orm_add_user, orm_add_to_cart
from luma.bot.aio_bot.python_hub_studio.lesson_7_part_2.filters.chat_types import ChatTypesFilter
from luma.bot.aio_bot.python_hub_studio.lesson_7_part_2.handlers.menu_processing import get_menu_content
from luma.bot.aio_bot.python_hub_studio.lesson_7_part_2.keyboards.inline import get_callback_btns, MenuCallBack

user_private_router = Router()
user_private_router.message.filter(ChatTypesFilter(['private']))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message, session: AsyncSession):
    media, reply_markup = await get_menu_content(session, level=0, menu_name="main")
    # функция вернет media из menu_processing  def main_menu, и вернет reply_markup

    await message.answer_photo(media.media, caption=media.caption, reply_markup=reply_markup)
    """ caption=media.caption - описание  и клавиатуру reply_markup 
    (media.media- потому что InputMediaPhoto содержит в себе изображение и описание 
    А в методе .answer_photo нужно передать  строу изображения и отдельно описание в параметр caption.

     """


async def add_to_cart(callback: types.CallbackQuery, callback_data: MenuCallBack, session: AsyncSession):
    user = callback.from_user  # получаем из callback  user-a
    await orm_add_user(  # добавляем юзера в БД
        session,
        user_id=user.id,
        first_name=user.first_name,
        last_name=user.last_name,
        phone=None,
    )
    await orm_add_to_cart(session, user_id=user.id, product_id=callback_data.product_id)
    await callback.answer("Товар добавлен в корзину.")


@user_private_router.callback_query(MenuCallBack.filter())  # класс MenuCallBack из  файла inline.
# фильтруем callback получаем его в хендлер
async def user_menu(callback: types.CallbackQuery, callback_data: MenuCallBack, session: AsyncSession):

    if callback_data.menu_name == "add_to_cart":
        await add_to_cart(callback, callback_data, session)
        return

    media, reply_markup = await get_menu_content(
        session,
        level=callback_data.level,
        menu_name=callback_data.menu_name,
        category=callback_data.category,
        page=callback_data.page,
        product_id=callback_data.product_id,
        user_id=callback.from_user.id,
    )

    await callback.message.edit_media(media=media, reply_markup=reply_markup)
    await callback.answer()

"""  заглушка функции - ...  три точки 
у нас есть список в async def user_menu
 level=callback_data.level,
        menu_name=callback_data.menu_name,
        category=callback_data.category,
        page=callback_data.page,
        product_id=callback_data.product_id,
        user_id=callback.from_user.id,
        
 добавляем category=callback_data.category, и записываем ее в  файл menu_proc  def get_menu_content. списки похожи
 async def get_menu_content(
        session: AsyncSession,
        level: int,
        menu_name: str,
        category: int | None = None,
        page: int | None = None,
        product_id: int | None = None,
        user_id: int | None = None,
        
 category: int | None = None,  #  т.к кнопки будут вести на следующий уровень меню пишем в 
 async def get_menu_content(.......):
  elif level == 2:
        return await products(session, level, category, page)

"""
