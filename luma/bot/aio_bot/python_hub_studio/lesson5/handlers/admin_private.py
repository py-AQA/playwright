from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from luma.bot.aio_bot.python_hub_studio.lesson5.keyboards.reply_les5 import get_keyboard
from luma.bot.aio_bot.python_hub_studio.lesson5.filters.chat_types_5 import ChatTypesFilter, IsAdmin

admin_router = Router()
admin_router.message.filter(ChatTypesFilter(["private"]), IsAdmin())


# ADMIN_KB будет передаваться несколько раз, формируем её здесь как константу
ADMIN_KB = get_keyboard(
    "Добавить товар",
    "Изменить товар",
    "Удалить товар",
    "Я так, просто посмотреть зашел",
    placeholder="Выберите действие",
    sizes=(2, 1, 1), )


@admin_router.message(Command("admin"))
async def add_product(message: types.Message):
    await message.answer("Что хотите сделать?", reply_markup=ADMIN_KB)


@admin_router.message(F.text == "Я так, просто посмотреть зашел")
async def starring_at_product(message: types.Message):
    await message.answer("ОК, вот список товаров")


@admin_router.message(F.text == "Изменить товар")
async def change_product(message: types.Message):
    await message.answer("ОК, вот список товаров")


@admin_router.message(F.text == "Удалить товар")
async def delete_product(message: types.Message):
    await message.answer("Выберите товар(ы) для удаления")


# Код ниже для машины состояний (FSM) СМОТРИ ОПИСАНИЕ ВНИЗУ

class AddProduct(StatesGroup):
    name = State()
    description = State()
    price = State()
    image = State()

    texts = {
        'AddProduct:name': 'Введите название заново:',
        'AddProduct:description': 'Введите описание заново:',
        'AddProduct:price': 'Введите стоимость заново:',
        'AddProduct:image': 'Этот стейт последний, поэтому...',
    }


# Становимся в состояние ожидания ввода name
@admin_router.message(StateFilter(None), F.text == "Добавить товар")
async def add_product(message: types.Message, state: FSMContext):
    # Реакция на кнопку "Добавить товар"- ожидание что юзер введет название конкретного товара пишем "Введите название
    # товара" и удаляем нашу кнопочную клавиатуру, что бы отобразилась обычная клавиатура ввода текста.
    # Это состояние ожидания ответа
    await message.answer(
        "Введите название товара", reply_markup=types.ReplyKeyboardRemove()
    )
    # Становимся в режим ожидания
    await state.set_state(AddProduct.name)


@admin_router.message(StateFilter("*"), Command("отмена"))
@admin_router.message(StateFilter("*"), F.text.casefold() == "отмена")
async def cancel_handler(message: types.Message, state: FSMContext) -> None:

    current_state = await state.get_state()
    if current_state is None:
        return

    await state.clear()
    await message.answer("Действия отменены", reply_markup=ADMIN_KB)

    """ Делаем проверку, StateFilter("*") что любые state допустимы,
    если юзер находится в каком-то из этих состояний 
метод casefold - работает как lower , но поддерживает большее количество символов
если админ ввел это тест сообщение или команду "отмена"  но у него нет активного диалога (отсутствует состояние), 
то завершаем работу этого хендлера , в ином случае
 state.clear() -сбрасываем состояние  
 и отправляем смс "Действия отменены" и возвращаем раскладку клавиатуры  для работы с товаром

ФУНКЦИЯ "ОТМЕНА" ОБНУЛЯЕТ ВСЮ ИНФОРМАЦИЮ, НУЖНО ВВОДИТЬ ВСЕ СНАЧАЛА
"""


# Вернутся на шаг назад (на прошлое состояние)
@admin_router.message(StateFilter("*"), Command("назад"))
@admin_router.message(StateFilter("*"), F.text.casefold() == "назад")
async def back_step_handler(message: types.Message, state: FSMContext) -> None:

    current_state = await state.get_state()  # Получаем текущее состояние

    if current_state == AddProduct.name:  # Возвращаться назад некуда
        await message.answer("Предыдущего шага нет, введите название товара или напишите отмена")
        return
# Нужно получить предыдущее состояние которое было
    previous = None
    # Проходимся по всем состояниям циклом
    for step in AddProduct.__all_states__:
        if step.state == current_state:
            await state.set_state(previous)  # Если условие выше выполняется, то мы приравниваем его к (previous)
            await message.answer(f"ок, вы вернулись к прошлому шагу \n {AddProduct.texts[previous.state]}")
            return
        previous = step


# Ловим данные для состояния name и потом меняем состояние на description
# Ожидаем что будет введен текст. Нужно этот текст перехватить, записать в хранилище,
# отправить юзеру "Введите описание товара" и встать в состояние ожидания ввода описания товара
@admin_router.message(AddProduct.name, F.text)
async def add_name(message: types.Message, state: FSMContext):
    if len(message.text) >= 100:
        await message.answer("Название товара не должно превышать 100 символов. \n Введите заново")
        return

    await state.update_data(name=message.text)  # Приняли имя товара
    await message.answer("Введите описание товара")
    await state.set_state(AddProduct.description)  # ожидаем ввода описания


# Хендлер для отлова некорректных вводов для состояния name
@admin_router.message(AddProduct.name)
async def add_name_2(message: types.Message, state: FSMContext):
    await message.answer("Вы ввели не допустимые данные, введите текст названия товара")


# Ловим данные для состояния description и потом меняем состояние на price
@admin_router.message(AddProduct.description, F.text)  # Проверка состояния, что готовы принять описание
# описание товара записываем в хранилище,
# отправляем юзеру "Введите стоимость товара" и становимся в состояние ожидания ввода стоимость товара
async def add_description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)  # Приняли описание
    await message.answer("Введите стоимость товара")
    await state.set_state(AddProduct.price)


# Хендлер для отлова некорректных вводов для состояния description
@admin_router.message(AddProduct.description)
async def add_description2(message: types.Message, state: FSMContext):
    await message.answer("Вы ввели не допустимые данные, введите текст описания товара")


# Ловим данные для состояния price и потом меняем состояние на image
@admin_router.message(AddProduct.price, F.text)
async def add_price(message: types.Message, state: FSMContext):
    try:
        float(message.text)
    except ValueError:
        await message.answer("Введите корректное значение цены")
        return

    # ожидаем загрузку фото
    await state.update_data(price=message.text)
    await message.answer("Загрузите изображение товара")
    await state.set_state(AddProduct.image)


# Хендлер для отлова некорректных данных ввода состояния price
@admin_router.message(AddProduct.price)
async def add_price2(message: types.Message, state: FSMContext):
    await message.answer("Вы ввели не допустимые данные, введите стоимость товара")


# Ловим данные для состояния image и потом выходим из состояний
@admin_router.message(AddProduct.image, F.photo)
async def add_image(message: types.Message, state: FSMContext):
    # ждем фото, после добавления всех данных в Базу Данных отправляем клавиатуру админа
    await state.update_data(image=message.photo[-1].file_id)

    """ 
    Если  админ отправляет F.photo
    state.update_data(image=message.photo[-1].file_id) 
    когда вы отправляете фото, изображение на серверах телеграмма обрабатывается в разных разрешениях 
    (они  перечислены в виде списка). 
    photo[-1] формат с самым большим разрешением. 
    """
    await message.answer("Товар добавлен", reply_markup=ADMIN_KB)
    data = await state.get_data()  # получаем словарь с нашими значениями
    await message.answer(str(data))  # отправим наши данные в чат в виде str
    await state.clear()  # очистка состояний пользователя и удаление данных из машины состояний


@admin_router.message(AddProduct.image)
async def add_image2(message: types.Message, state: FSMContext):
    await message.answer("Отправьте фото пищи")



"""
Хендлеры которые для админа, должны  работать только для админа. Делаем чат фильтр  isAdmin.
В фильтре проверяем, находится ли написавший в списке админов. 
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


"""Машина состояний!:
ПЕРЕД РАБОТОЙ С ХЕНДЛЕРАМИ НАДО ОПИСАТЬ ШАГИ РАБОТЫ
создаем класс Addproduct импорт от класса StatesGroup. Перечисляем  в классе пункты (шаги), которые нам нужны.

name = State()
description = State()
price = State()
image = State()


Каждой переменной задаем класс State
from aiogram.fsm.state import StatesGroup, State

Эти переменные по сути- состояние каждого отдельного пользователя

Кроме меседж, в хендлер надо передать State самого пользователя
async def add_image(message: types.Message, state: FSMContext):
Чтоб в зависимости данных. которые сюда придут, оперировать состояниями пользователей

Админ вводит команду "Добавить товар". Первое что нужно проверить, кроме текста на соответствие введенной команды,
Что у польз-ля нет активных состояний  @admin_router.message(StateFilter(None), F.text == "Добавить товар")
  # Становимся в режим ожидания
    await state.set_state(Addproduct.name)


В хендлере где отлавливаем это событие пишем проверку на это состояние Пример:
# Ожидаем что будет введен текст. Нужно этот текст перехватить, записать в хранилище,
@admin_router.message(Addproduct.name, F.text)

async def add_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text) -получить название товара 
    await message.answer("Введите описание товара") -отправляем  смс а

await state.set_state(Addproduct.description)  # ожидаем ввода описания / меняем состояние юзера
    

В wait state.update_data(name=message.text) записываются полученные от юзера данные
name товара берется из message.text, на выходе в этом stat-e будет словарь с данными

Дальше последовательные действия с проверкой состояния и ожиданием ввода

В начале функции проверяем  что мы в нужном состоянии, приимаем данные с предыдущей функции, записываем данные
ниже отправляем смс и становимся в состояние ожидания ввода следующего шага, который будет в функции  ниже.
"""
