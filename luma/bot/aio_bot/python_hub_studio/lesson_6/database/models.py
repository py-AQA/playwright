

"""====================================Создание таблиц==============================================="""
from sqlalchemy import DateTime, Float, String, Text, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):  # Наследуемся от класса из библиотеки
    # указывает дату создания - текущую дату и время
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())

    # указывает дату изменения
    updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())


class Product(Base):
    __tablename__ = 'product'

# создаем поля
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str] = mapped_column(Text)
    price: Mapped[float] = mapped_column(Float(asdecimal=True), nullable=False)
    image: Mapped[str] = mapped_column(String(150))  # Id изображения, а не картинка, длина строки до 150 символов


"""
Ставим аннотацию с помощью класса Mapped, не вызываем его.
указываем primary_key=True,  и авто-увеличение поля на 1 при заполнении autoincrement=True)
Для поля name надо указать ограничение на количество символов, макс = 150 символов, nullable=False не может быть пустым
Для поля  description, что это поле текст, а не varchar

"""








