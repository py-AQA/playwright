from aiogram.types import KeyboardButtonPollType, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Menu"),
            KeyboardButton(text="about shop"),
            KeyboardButton(text="delivery options"),
            KeyboardButton(text="payment options"),
        ],
    ],
    resize_keyboard=True, input_field_placeholder="What do you interesting?"
)
