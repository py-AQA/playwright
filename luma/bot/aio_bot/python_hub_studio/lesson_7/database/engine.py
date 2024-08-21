"""===============================Подготовка движка ORM============================================================"""

import os

from dotenv import load_dotenv, find_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from .models import Base
from luma.bot.aio_bot.python_hub_studio.lesson_7.database.orm_query import orm_create_categories, orm_add_banner_description
from luma.bot.aio_bot.python_hub_studio.lesson_7.texts_for_db import categories, description_for_info_pages

load_dotenv(find_dotenv())

# engine = create_async_engine(os.getenv('DB_LITE'), echo=True)
"""echo=True выводит все запросы в терминал"""

engine = create_async_engine(os.getenv('DB_URL'), echo=True)

session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
"""bind=engine - движок который инициализировали
class_=AsyncSession - асинхронный метод создания сессии
expire_on_commit=False) - для  повторной возможности воспользоваться сессией после коммита, чтоб сессия не закрывалась.

Чтоб система orm создавала таблицу которая описана в файле models пишем функцию:
"""


async def create_db():  # Запускаем функции в lesson_7
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        # conn.run_sync В SqlAlchemy нет этого метода в асинхронном варианте нет
        # (Base.metadata.create_all) Обращаемся к классу Base из файла models, чтоб создать все таблицы

    """ открываем сессию и используем функции orm_create_categories, orm_add_banner_description, чтобы при старте 
    они были записаны в БД, в том числе и описание для страниц банеров
    orm запросы написаны так, что если там уже есть записи, то этого происходить не будет
     """

    async with session_maker() as session:
        await orm_create_categories(session, categories)
        await orm_add_banner_description(session, description_for_info_pages)


async def drop_db():  # Если нужно удалить все таблицы
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
