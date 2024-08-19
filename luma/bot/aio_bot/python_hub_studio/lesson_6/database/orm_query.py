
""" Здесь запросы на ввод информации для нового товара , данные которые будут сохраняться в БД """
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from luma.bot.aio_bot.python_hub_studio.lesson_6.database.models import Product


async def orm_add_product(session: AsyncSession, data: dict):
    obj = Product(
        name=data["name"],
        description=data["description"],
        price=float(data["price"]),
        image=data["image"],
    )
    session.add(obj)
    await session.commit()


# делаем select sql и возвращаем в хендлер result.scalars().all()
async def orm_get_products(session: AsyncSession):
    query = select(Product)
    result = await session.execute(query)
    return result.scalars().all()


# делаем select на отдельный продукт
async def orm_get_product(session: AsyncSession, product_id: int):
    query = select(Product).where(Product.id == product_id)
    result = await session.execute(query)
    return result.scalar()


# обновить данные продукта
async def orm_update_product(session: AsyncSession, product_id: int, data):
    query = update(Product).where(Product.id == product_id).values(
        name=data["name"],
        description=data["description"],
        price=float(data["price"]),
        image=data["image"],)
    await session.execute(query)
    await session.commit()  # закрепление данных в БД


# удаление товара
async def orm_delete_product(session: AsyncSession, product_id: int):
    query = delete(Product).where(Product.id == product_id)
    await session.execute(query)
    await session.commit()
