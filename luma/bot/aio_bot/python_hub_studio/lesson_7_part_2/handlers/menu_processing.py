from aiogram.types import InputMediaPhoto
from sqlalchemy.ext.asyncio import AsyncSession

from luma.bot.aio_bot.python_hub_studio.lesson_7_part_2.database.orm_query import (
    orm_add_to_cart,
    orm_delete_from_cart,
    orm_get_banner,
    orm_get_categories,
    orm_get_products,
    orm_get_user_carts,
    orm_reduce_product_in_cart,
)
from luma.bot.aio_bot.python_hub_studio.lesson_7_part_2.keyboards.inline import (
    get_products_btns,
    get_user_cart,
    get_user_catalog_btns,
    get_user_main_btns,
)

from luma.bot.aio_bot.python_hub_studio.lesson_7_part_2.general.paginator import Paginator


async def main_menu(session, level, menu_name):
    banner = await orm_get_banner(session, menu_name)  # передаем сессию и menu_name, тут будет строка main,
    # по этой строке  из Бд возьмем id изображения
    image = InputMediaPhoto(media=banner.image, caption=banner.description)
    # подгружаем фото с описанием из аiogram types ,получаем экземпляр с БД,
    # потом получаем id изображения  media=banner.image и описание  caption=banner.description

    kbds = get_user_main_btns(level=level)  # создаем кнопки для этого уровня меню, пишем актуальный левел,
    # сюда придет Ноль из параметров хендлера.  Одноименная функция в файле inline

    return image, kbds


"""return image, kbds вернется в user_private start_cmd"""


async def catalog(session, level, menu_name):
    banner = await orm_get_banner(session, menu_name)  # формируем банер по  menu_name
    image = InputMediaPhoto(media=banner.image, caption=banner.description)

    categories = await orm_get_categories(session)  # получаем из БД  категории товаров
    kbds = get_user_catalog_btns(level=level, categories=categories)

    return image, kbds


def pages(paginator: Paginator):
    btns = dict()
    if paginator.has_previous():
        btns["◀ Пред."] = "previous"

    if paginator.has_next():
        btns["След. ▶"] = "next"

    return btns


async def products(session, level, category, page):
    products = await orm_get_products(session, category_id=category)

    paginator = Paginator(products, page=page)
    """class paginator
    array: list | tuple,
             page: int = 1, какую сейчас отображать страницу
             per_page: int = 1) -> None  - сколько товаров выводить на страницу  """
    product = paginator.get_page()[0]  # возвращается список, берем по индексу

    image = InputMediaPhoto(
        media=product.image,
        caption=f"<strong>{product.name}\
                </strong>\n{product.description}\nСтоимость: {round(product.price, 2)}\n\
                <strong>Товар {paginator.page} из {paginator.pages}</strong>",
    )
    """ <strong>Товар {paginator.page} из {paginator.pages}</strong>",
    отобразить юзеру- какой это товар по счету
      """
    pagination_btns = pages(paginator)

    kbds = get_products_btns(
        level=level,
        category=category,
        page=page,
        pagination_btns=pagination_btns,
        product_id=product.id,
    )

    return image, kbds


async def carts(session, level, menu_name, page, user_id, product_id):  # session - для взаимодействия с БД.
    # level, menu_name что понять на каком уровне/странице происходит действие.
    # menu_name= delete/decrement"/"increment"
    # прописаны в кнопках, в файле inline def get_user_cart /if page:/callback_data=...(level=level, menu_name='delete'
    # page для пагинатора, user_id -отфильтровать корзины klz конкретного юзера,
    # product_id - для удаления конкретного продукта(пробрасывается в кнопках через callback data)
    if menu_name == "delete":
        await orm_delete_from_cart(session, user_id, product_id)
        if page > 1:
            page -= 1

    elif menu_name == "decrement":  # Если  юзер нажмет на кнопку "-1"
        is_cart = await orm_reduce_product_in_cart(session, user_id, product_id)
        if page > 1 and not is_cart:
            page -= 1

    elif menu_name == "increment":
        await orm_add_to_cart(session, user_id, product_id)

    carts = await orm_get_user_carts(session, user_id)

    if not carts:  # если корзин нет , показываем дефолтный банер корзины
        # и отображаться 1 кнопка - вернуться на главную страницу
        banner = await orm_get_banner(session, "cart")
        image = InputMediaPhoto(
            media=banner.image, caption=f"<strong>{banner.description}</strong>"
        )

        kbds = get_user_cart(
            level=level,
            page=None,
            pagination_btns=None,
            product_id=None,
        )

    else:  # корзина есть
        paginator = Paginator(carts, page=page)

        cart = paginator.get_page()[0]

        cart_price = round(cart.quantity * cart.product.price, 2)
        total_price = round(
            sum(cart.quantity * cart.product.price for cart in carts), 2
        )
        image = InputMediaPhoto(
            media=cart.product.image,
            caption=f"<strong>{cart.product.name}</strong>\n{cart.product.price}$ x {cart.quantity} = {cart_price}$\
                    \nТовар {paginator.page} из {paginator.pages} в корзине.\nОбщая стоимость товаров в корзине {total_price}",
        )

        pagination_btns = pages(paginator)

        kbds = get_user_cart(
            level=level,
            page=page,
            pagination_btns=pagination_btns,
            product_id=cart.product.id,
        )

    return image, kbds


async def get_menu_content(
        session: AsyncSession,
        level: int,
        menu_name: str,
        category: int | None = None,
        page: int | None = None,
        product_id: int | None = None,
        user_id: int | None = None,
):
    if level == 0:
        return await main_menu(session, level, menu_name)
    elif level == 1:  # запускаем функцию get_user_catalog_btns в файле inline
        return await catalog(session, level, menu_name)
    elif level == 2:
        return await products(session, level, category, page)
    elif level == 3:
        return await carts(session, level, menu_name, page, user_id, product_id)

    """задача  def get_menu_content принять все аргументы от обработчика из user_private функции def start_cmd"""
