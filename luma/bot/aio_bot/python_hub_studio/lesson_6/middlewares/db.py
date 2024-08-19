from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message
from sqlalchemy.ext.asyncio import async_sessionmaker


class DataBaseSession(BaseMiddleware):
    def __init__(self, session_pool: async_sessionmaker):
        self.session_pool = session_pool

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        async with self.session_pool() as session:
            data['session'] = session
            return await handler(event, data)


class CounterMiddleware(BaseMiddleware):
    """ Название любое, обязательно наследуемся от BaseMiddleware
    def __init__ отрабатывает 1 раз при старте бота, когда происходит регистрация middleware слоя
    """

    def __init__(self) -> None:
        self.counter = 0

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            # автоматически приходит экземпляр хендлера
            event: Message,  # какое было событие
            data: Dict[str, Any]  # словарь содержащий все что может передаваться в хендлер (также с middleware слоев)
    ) -> Any:
        self.counter += 1
        data['counter'] = self.counter  # передаем переменную counter в словарь
        return await handler(event, data)  # передаем по цепочке обработку данных (событие и словарь data)


class CounterMiddleware2(BaseMiddleware):
    def __init__(self) -> None:
        self.counter = 0

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        self.counter += 1
        data['counter'] = self.counter
        return await handler(event, data)


"""  ===========================================================================================================
Здесь  можно проверить user id" пример из chat gpt
class CounterMiddleware2(BaseMiddleware):
    def __init__(self) -> None:
        self.counter = 0

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        self.counter += 1
        data['counter'] = self.counter
        
        # Проверка user ID
        user_id = event.from_user.id if hasattr(event, 'from_user') and event.from_user else None
        
        if user_id is not None:
            print(f"User ID: {user_id}")
        else:
            print("User ID не найден.")
        
        return await handler(event, data)
        
Объяснение кода
Доступ к user ID:
Внутри метода __call__, мы проверяем, есть ли атрибут from_user в объекте event.
Если from_user существует, мы можем получить user ID через event.from_user.id.
Обработка отсутствия user ID:
Если from_user отсутствует, мы выводим сообщение о том, что user ID не найден. Это поможет вам избежать ошибок, 
связанных с отсутствием данных.
Важно
Убедитесь, что объект TelegramObject действительно содержит информацию о пользователе в нужном формате. 
Это зависит от того, как вы интегрировали и настроили ваш бот.
Если структура TelegramObject отличается, возможно, потребуется адаптировать код для правильного доступа к user ID.
==================================================================================================================
"""

""" Функцию счетчик  применили в admin_private  в хендлере  

@admin_router.message(F.text == "Удалить товар")
async def delete_product(message: types.Message, counter):
    print(counter)
    await message.answer("Выберите товар(ы) для удаления")
    
После чего при нажатии кнопки  "Удалить товар "в чате бота, пишется количество нажатий на эту кнопку, 
после каждого клика.

==================================================================================================================

Разница между двумя классами CounterMiddleware и CounterMiddleware2 заключается в типах объектов, которые они 
обрабатывают в методе __call__. Давайте рассмотрим это подробнее.

                                   1. Классы и их конструкции
CounterMiddleware:
В этом классе метод __call__ принимает параметр event типа Message.
Это означает, что этот middleware предназначен для работы непосредственно с объектами сообщений, 
поступающими от пользователей.


CounterMiddleware2:
Здесь метод __call__ принимает параметр event типа TelegramObject.
Это более общий класс, который может содержать информацию о различных событиях, связанных с ботом, 
не только о сообщениях.

                                          2. Разница в обработке событий
CounterMiddleware:
Поскольку   CounterMiddleware работает с типом Message, он предназначен для обработки событий, связанных именно 
с текстовыми сообщениями или сообщениями других типов (например, фото, видео и т.д.), 
но в рамках конкретной структуры сообщений.
Это ограничивает его использование только к событиям, связанным с сообщениями.


CounterMiddleware2:
Используя TelegramObject, этот middleware может обрабатывать более широкий спектр событий, поскольку TelegramObject
может включать разные типы событий, такие как нажатия кнопок, обновления статуса и другие.
Это делает CounterMiddleware2 более универсальным и гибким в контексте обработки событий.

                                              3. Применение
Когда использовать CounterMiddleware?
Если ваша логика обработки строго связана с событиями сообщений и вам не нужно обрабатывать другие типы событий.

Когда использовать CounterMiddleware2?
Если вам нужно обрабатывать более широкий диапазон событий и передавать информацию о событиях в обработчики, включая, 
но не ограничиваясь, текстовыми сообщениями.
====================================================================================================================
"""
