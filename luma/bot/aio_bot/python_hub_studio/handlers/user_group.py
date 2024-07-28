from string import punctuation

from aiogram import types, Router
from luma.bot.aio_bot.python_hub_studio.filters.chat_types import ChatTypesFilter

user_group_router = Router()
user_group_router.message.filter(ChatTypesFilter(["group"]))
restricted_words = {'boar', 'hamster', 'muskrat'}

""" Проверка чата на запрещенные слова - restricted_words, удаления  запрещенного смс юзера . предупреждение юзера
закомментирована строка Бан
"""


def clean_text(text: str):
    return text.translate(str.maketrans("", "", punctuation))


@user_group_router.edited_message()
@user_group_router.message()
async def cleaner(message: types.Message):
    # функция модерации по умолчанию
    # if restricted_words.intersection(message.text.lower().split()):

    # условия проверки на запрещенные слова несмотря на маскировку другими знаками
    if restricted_words.intersection(clean_text(message.text.lower()).split()):
        await message.answer(f'{message.from_user.first_name}, keep order in the chat!')
        await message.delete()
        # await  message.chat.ban(message.from_user.id)  Забанить юзера
