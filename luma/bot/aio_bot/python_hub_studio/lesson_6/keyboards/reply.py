from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_keyboard(
        *btns: str,
        # Есть переменная btns, куда передаем через запятую, то что быть написано на кнопках
        placeholder: str = None,
        # Сформировать кнопку для запроса контакта или местоположения юзера, передается индекс кнопки
        request_contact: int = None,
        request_location: int = None,
        sizes: tuple[int] = (2,), ):
        # sizes: (list[int]) = (2,), ):
    """
    Parameters request_contact and request_location must be as indexes of btns (buttons) args for buttons you need.
    Example:
    get_keyboard(
            "Меню",
            "О магазине",
            "Варианты оплаты",
            "Варианты доставки",
            "Отправить номер телефона"
            placeholder="Что вас интересует?",
            request_contact=4,
            sizes=(2, 2, 1)     # 2 кнопки в 1м ряду, 2 кнопки во 2м ряду, 1 кнопка в 3м ряду
        )
        "Отправить номер телефона" пятая кнопка, но индекс 4
    """
    # Формируется клавиатура
    keyboard = ReplyKeyboardBuilder()
    # автоматическая генерация индексов каждой кнопки
    for index, text in enumerate(btns, start=0):

        if request_contact and request_contact == index:
            keyboard.add(KeyboardButton(text=text, request_contact=True))

        elif request_location and request_location == index:
            keyboard.add(KeyboardButton(text=text, request_location=True))
        else:
            keyboard.add(KeyboardButton(text=text))

    # передается *sizes (сколько рядов кнопок и количество в ряду), а также placeholder
    # resize_keyboard=True авто-подгонка размера кнопки
    return keyboard.adjust(*sizes).as_markup(
        resize_keyboard=True, input_field_placeholder=placeholder)


"""
Создаем функцию, которая генерирует любые кнопки
        
"""
