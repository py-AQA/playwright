from string import punctuation

from aiogram import types, Router, Bot, F
from aiogram.filters import Command

from luma.bot.aio_bot.python_hub_studio.lesson_7_part_2.filters.chat_types import ChatTypesFilter

user_group_router = Router()
user_group_router.message.filter(ChatTypesFilter(["group", "supergroup"]))
user_group_router.edited_message.filter(ChatTypesFilter(["group", "supergroup"]))

restricted_words = {'boar', 'hamster', 'muskrat'}
""" Проверка чата на запрещенные слова - restricted_words, удаления  запрещенного смс юзера . предупреждение юзера
закомментирована строка Бан
"""


@user_group_router.message(Command("admin"))
async def get_admins(message: types.Message, bot: Bot):
    chat_id = message.chat.id
    # получаем chat.id, формируем админ лист

    admins_list = await bot.get_chat_administrators(chat_id)
    member_list = await bot.get_chat_member(user_id=673432417, chat_id=chat_id)
    # передаем chat.id, бот получает список от сервера
    # В списке будут creator и administrator
    print(admins_list)
    print(member_list)

    admins_list = [
        member.user.id
        for member in admins_list
        if member.status == "creator" or member.status == "administrator"
    ]
    bot.my_admins_list = admins_list
    if message.from_user.id in admins_list:
        await message.delete()
    print(admins_list)

"""  В фильтре проверяем, находится ли написавший в списке админов. 
Если написавший есть в админ листе, то удалить эту команду
Каждый  раз при проверке админа, не нужно делать запрос к API.
 
На команду admin  отправляется клавиатура  с действиями для самого админа.
Такая же команда admin  есть  у нас в группе.
Запускаем бота,если  напишем ему в личку /admin, то клавиатуру админа сразу не покажет. 
Фильтр isAdmin не работает, нет списка админов.
Переходим в группу с ботом, отправляем команду /admin, бот удаляет её в чате и отправляет список из админов и владельца.

bot.my_admins_list = admins_list получает список.
Заходим в личку к боту и отправляем /admin  и получаем клавиатуру админа.

ПРЕИМУЩЕСТВА!:
Гибко менять список админов.
Запрос к API телеграмма делается 1 раз при запросе списка в группе
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
