
"""====================================Создание таблиц==============================================="""
from sqlalchemy import func, DateTime, ForeignKey, Numeric, String, Text, BigInteger
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):  # Наследуемся от класса из библиотеки
    # указывает дату создания - текущую дату и время
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())

    # указывает дату изменения
    updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())


class Banner(Base):  # картинки товаров пиццерии
    __tablename__ = 'banner'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(15), unique=True)
    image: Mapped[str] = mapped_column(String(150), nullable=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)


class Category(Base):  # выбор категории: еда, напитки
    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)


# создаем поля
class Product(Base):  # таблица продуктов
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str] = mapped_column(Text)
    price: Mapped[float] = mapped_column(Numeric(5, 2), nullable=False)
    # Numeric(5, 2 ) может быть 5 знаков, 2 знака до запятой: = 7.99

    image: Mapped[str] = mapped_column(String(150))
    category_id: Mapped[int] = mapped_column(ForeignKey('category.id', ondelete='CASCADE'), nullable=False)
    # ForeignKey - внешний ключ - ссылка на таблицу 'category' поле id
    # ondelete='CASCADE' - когда удаляется категория , будут удалены все продукты

    category: Mapped['Category'] = relationship(backref='product')
    # relationship(backref='product') -связь, чтоб делать выборку


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    user_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    # id в телеграмме

    first_name: Mapped[str] = mapped_column(String(150), nullable=True)
    last_name: Mapped[str] = mapped_column(String(150), nullable=True)
    phone: Mapped[str] = mapped_column(String(13), nullable=True)


class Cart(Base):  # корзина юзера
    __tablename__ = 'cart'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)  # id записи в БД
    user_id: Mapped[int] = mapped_column(ForeignKey('user.user_id', ondelete='CASCADE'), nullable=False)

    """ ForeignKey('user.user_id' - ключ на  class User(Base): поле user_id (телеграмме)
    Как только юзер удален из БД , будут удалены все корзины """

    product_id: Mapped[int] = mapped_column(ForeignKey('product.id', ondelete='CASCADE'), nullable=False)
    quantity: Mapped[int]  # поле количество
    """ ForeignKey связывает 2 таблицы  class User(Base): и class Cart(Base): с одноименными полями
    Как только товар  удален из БД , будут удалены все корзины с этим товаром"""

    user: Mapped['User'] = relationship(backref='cart')
    product: Mapped['Product'] = relationship(backref='cart')
    """ через  relationship делаем взаимосвязь с таблицами  user и  product
    Если юзер закажет 3 разных товара, то будет 3 корзины и в каждой будет лежать отдельный  товар product:id 
     и его количество. В итоге мы будем брать информацию с всех записей"""


"""
Ставим аннотацию с помощью класса Mapped, не вызываем его.
указываем primary_key=True,  и авто-увеличение поля на 1 при заполнении autoincrement=True)
Для поля name надо указать ограничение на количество символов, макс = 150 символов, nullable=False не может быть пустым
Для поля  description, что это поле текст, а не varchar

"""
