from aiogram.types import KeyboardButtonPollType, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Menu"),
            KeyboardButton(text="About shop"),
        ],
        {
            KeyboardButton(text="Delivery options"),
            KeyboardButton(text="Payment options"),
        },
    ],
    resize_keyboard=True,
    input_field_placeholder="What do you interesting?"
)

del_kbd = ReplyKeyboardRemove()
# del_kbd = ReplyKeyboardRemove() -  удаляет клавиатуру

start_kb2 = ReplyKeyboardBuilder()
start_kb2.add(
    KeyboardButton(text="Меню"),
    KeyboardButton(text="О магазине"),
    KeyboardButton(text="Варианты доставки"),
    KeyboardButton(text="Варианты оплаты"),
)
start_kb2.adjust(2, 2)
# start_kb2.adjust(2, 2) сколько кнопок в каком ряду хотим разместить-
# т.е 2 кнопки в первом ряду и 2 кнопки во втором ряду


start_kb3 = ReplyKeyboardBuilder()
start_kb3.attach(start_kb2)
# обращаемся к клавиатуре(start_kb2)

start_kb3.row(KeyboardButton(text="Оставить отзыв"))
# row добавить кнопку рядом - это широкая кнопка на всю третью строку (ряд)

test_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Создать опрос", request_poll=KeyboardButtonPollType()),
        ],
        [
            KeyboardButton(text="Отправить номер ☎️", request_contact=True),
            KeyboardButton(text="Отправить локацию 🗺️", request_location=True),
        ],
    ],
    resize_keyboard=True,
)

