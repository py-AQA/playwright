""" https://www.youtube.com/watch?v=qfNRbyvx5Uo&list=PLNi5HdK6QEmWLtb8gh8pwcFUJCAabqZh_&index=8"""


from aiogram import types, Router, F
from aiogram.filters import CommandStart

from luma.bot.aio_bot.python_hub_studio.lesson_7.filters.chat_types import ChatTypesFilter
from luma.bot.aio_bot.python_hub_studio.lesson_7.keyboards.inline import get_callback_btns

user_private_router = Router()
user_private_router.message.filter(ChatTypesFilter(['private']))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Привет, я виртуальный помощник",
                         reply_markup=get_callback_btns(btns={  # формируем инлайн кнопку
                             'Нажми меня': 'some_1'   # и какую-то callback data
                         }))


@user_private_router.callback_query(F.data.startswith('some_'))
async def counter(callback: types.CallbackQuery):
    number = int(callback.data.split('_')[-1])  # перехватываем эту callback data разбиваем по "_" и выводим последнюю

    await callback.message.edit_text(  # собираемся отредактировать полученный текст
        text=f"Нажатий - {number}",  # передаем тест нажатий "number"

        reply_markup=get_callback_btns(btns={   # передаем клавиатуру с новым текстом
            'Нажми еще раз': f'some_{number + 1}'  # меняем текст какой-то callback data на {number + 1}
        }))

""" await callback.message. дает варианты :
edit_reply_markup() - отредактировать кнопки под сообщением
edit_caption() - отредактировать описание 
.edit_media() - отредактировать изображение, документ - все что относится к медиа. 

Текст нельзя заменить на изображение.
У телеграмма ограничение на удаление смс бота пользователем - 48 часов, потом удалить нельзя.
А на редактирование  смс нет.
 Рекомендация- редактировать старые смс вместо удаления старых и отправки новых,
 чтоб чат с ботом не был захламлен старыми смс
"""

""