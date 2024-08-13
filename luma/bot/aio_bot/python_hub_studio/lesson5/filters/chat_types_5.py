from aiogram.filters import Filter
from aiogram import Bot, types


class ChatTypesFilter(Filter):
    def __init__(self, chat_types: list[str]) -> None:
        self.chat_types = chat_types

    async def __call__(self, message: types.Message) -> bool:
        return message.chat.type in self.chat_types


class IsAdmin(Filter):
    def __init__(self) -> None:
        pass

    async def __call__(self, message: types.Message, bot: Bot) -> bool:
        return message.from_user.id in bot.my_admins_list


# Принимаем смс и прокидываем объект бота. Получаем список админов этой группы (в которой бот участник) и сравниваем,
# если message.from_user.id в списке админов, то разрешать взаимодействовать с ботом и менять меню
