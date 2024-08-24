from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class MenuCallBack(CallbackData, prefix="menu"):
    # поля перечисленные в классе
    level: int
    menu_name: str
    category: int | None = None
    page: int = 1
    product_id: int | None = None


"""Под каждым товаром для кнопки купить нужно передавать product_id  
и на кнопках  пагинации отображать текущую страницу
 page: int = 1
 product_id: int | None = None
 и пишем то что будет  на кнопках в  def get_products_btns(), которая возвращает эти кнопки

"""


def get_user_main_btns(*, level: int, sizes: tuple[int] = (2,)):
    # (*, level: int, sizes: tuple[int] = (2,))  содержится в get_user_main_btns при наведении курсора
    # на kbds = get_user_main_btns(level=level) в файле  menu_processing  def main_menu

    keyboard = InlineKeyboardBuilder()
    btns = {
        "Товары 🍕": "catalog",
        "Корзина 🛒": "cart",
        "О нас ℹ️": "about",
        "Оплата 💰": "payment",
        "Доставка ⛵": "shipping",
    }
    for text, menu_name in btns.items():  # циклом перебираем словарь
        if menu_name == 'catalog':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=level + 1, menu_name=menu_name).pack()))
        elif menu_name == 'cart':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=3, menu_name=menu_name).pack()))
        else:
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=level, menu_name=menu_name).pack()))

    return keyboard.adjust(*sizes).as_markup()


def get_user_catalog_btns(*, level: int, categories: list, sizes: tuple[int] = (2,)):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(InlineKeyboardButton(text='Назад',
                                      callback_data=MenuCallBack(level=level - 1, menu_name='main').pack()))
    # кнопка назад ведет на уровень -1, мы возвращаемся на предыдущую страницу
    keyboard.add(InlineKeyboardButton(text='Корзина 🛒',
                                      callback_data=MenuCallBack(level=3, menu_name='cart').pack()))
    # Для кнопок выбора отдельной категории товаров. Проходимся по списку, "c" - это сокращение от category
    for c in categories:
        keyboard.add(InlineKeyboardButton(text=c.name,
                                          callback_data=MenuCallBack(level=level + 1, menu_name=c.name,
                                                                     category=c.id).pack()))
    # level=level + 1 , так как это следующий уровень меню, menu_name=c.name - указываем название категории
    # и указываем дополнительный callback - c.id для кнопки, чтоб выбрать товары из Бд принадлежащие этой категории
    return keyboard.adjust(*sizes).as_markup()


# функция вызывается в menu_processing def get_menu_content elif level == 1:


def get_products_btns(
        *,
        level: int,
        category: int,
        page: int,
        pagination_btns: dict,  # кнопки назад и вперед
        product_id: int,  # чтоб разместить callback data на кнопке купить
        sizes: tuple[int] = (2, 1)
):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(InlineKeyboardButton(text='Назад',
                                      callback_data=MenuCallBack(level=level - 1, menu_name='catalog').pack()))
    keyboard.add(InlineKeyboardButton(text='Корзина 🛒',
                                      callback_data=MenuCallBack(level=3, menu_name='cart').pack()))
    keyboard.add(InlineKeyboardButton(text='Купить 💵',
                                      callback_data=MenuCallBack(level=level, menu_name='add_to_cart',
                                                                 product_id=product_id).pack()))
# MenuCallBack(level=level, при покупке level не меняется
    keyboard.adjust(*sizes)

    row = []
    for text, menu_name in pagination_btns.items():
        if menu_name == "next":
            row.append(InlineKeyboardButton(text=text,
                                            callback_data=MenuCallBack(
                                                level=level,    # level не меняется
                                                menu_name=menu_name,
                                                category=category,
                                                page=page + 1).pack()))

        elif menu_name == "previous":
            row.append(InlineKeyboardButton(text=text,
                                            callback_data=MenuCallBack(
                                                level=level,
                                                menu_name=menu_name,
                                                category=category,
                                                page=page - 1).pack()))

    return keyboard.row(*row).as_markup()  # кнопки находятся в нижнем ряду


def get_user_cart(
        *,
        level: int,
        page: int | None,  # для пагинации, товаров может быть несколько в корзине
        pagination_btns: dict | None,  # кнопки "назад", "вперед "
        product_id: int | None,  # для кнопок "удалить" / изменения количества товара "-1" "+1"
        sizes: tuple[int] = (3,)  # кнопки в первом ряду
):
    keyboard = InlineKeyboardBuilder()
    if page:  # если товар в корзине
        keyboard.add(InlineKeyboardButton(text='Удалить',
                                          callback_data=MenuCallBack(level=level, menu_name='delete',
                                                                     product_id=product_id, page=page).pack()))
        keyboard.add(InlineKeyboardButton(text='-1',
                                          callback_data=MenuCallBack(level=level, menu_name='decrement',
                                                                     product_id=product_id, page=page).pack()))
        keyboard.add(InlineKeyboardButton(text='+1',
                                          callback_data=MenuCallBack(level=level, menu_name='increment',
                                                                     product_id=product_id, page=page).pack()))

        keyboard.adjust(*sizes)

        row = []
        for text, menu_name in pagination_btns.items():
            if menu_name == "next":
                row.append(InlineKeyboardButton(text=text,
                                                callback_data=MenuCallBack(level=level, menu_name=menu_name,
                                                                           page=page + 1).pack()))
                # + 1 у кнопки "след.", - 1 у кнопки "пред."
            elif menu_name == "previous":
                row.append(InlineKeyboardButton(text=text,
                                                callback_data=MenuCallBack(level=level, menu_name=menu_name,
                                                                           page=page - 1).pack()))

        keyboard.row(*row)  # добавляем ряд кнопок

        row2 = [
            InlineKeyboardButton(text='На главную 🏠',
                                 callback_data=MenuCallBack(level=0, menu_name='main').pack()),
            InlineKeyboardButton(text='Заказать',
                                 callback_data=MenuCallBack(level=0, menu_name='order').pack()),
        ]
        # menu_name='order' - заглушка кнопки "заказать". Пока функция "заказать" не реализована
        return keyboard.row(*row2).as_markup()
    else:
        keyboard.add(
            InlineKeyboardButton(text='На главную 🏠',
                                 callback_data=MenuCallBack(level=0, menu_name='main').pack()))

        return keyboard.adjust(*sizes).as_markup()


def get_callback_btns(*,  # автоматический запрет на передачу не именованных аргументов
                      btns: dict[str, str],
                      # Передаем словарь dict[str, str], с текстом и строкой данных внутри,
                      # которые будут отправляться боту при клике кнопки
                      sizes: tuple[int] = (2,)):
    keyboard = InlineKeyboardBuilder()

    for text, data in btns.items():
        keyboard.add(InlineKeyboardButton(text=text, callback_data=data))

    return keyboard.adjust(*sizes).as_markup()


""" Reply кнопки отправляют, то что на них написано .
А inline кнопки содержат метод text- это надпись на кнопке, но она не отправляется в чат.

можно передать URL,

callback data ( тип запроса callback query)  ,в которой мы задаем особое значение в виде str,
при нажатии на эту кнопку оно  отправляется в боту и мы его ловим хендлером
"""
