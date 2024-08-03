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
