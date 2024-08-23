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
