from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


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


def get_url_btns(*, btns: dict[str, str], sizes: tuple[int] = (2,)):
    keyboard = InlineKeyboardBuilder()

    for text, url in btns.items():
        keyboard.add(InlineKeyboardButton(text=text, url=url))

    return keyboard.adjust(*sizes).as_markup()


# Создать микс из CallBack и URL кнопок
def get_inline_mix_btns(*, btns: dict[str, str], sizes: tuple[int] = (2,)):
    keyboard = InlineKeyboardBuilder()

# если в словаре будет '://' - то делаем кнопку с url
    for text, value in btns.items():
        if '://' in value:
            keyboard.add(InlineKeyboardButton(text=text, url=value))
        else:
            keyboard.add(InlineKeyboardButton(text=text, callback_data=value))

    return keyboard.adjust(*sizes).as_markup()
