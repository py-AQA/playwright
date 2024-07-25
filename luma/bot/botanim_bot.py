import os
from typing import Final

from dotenv import load_dotenv
# from dotenv import dotenv_values
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CommandHandler, CallbackQueryHandler, ApplicationBuilder, CallbackContext

# settings: dict = dotenv_values(".env")
# bot_token = settings.get("TOKEN")

load_dotenv()
bot_token = os.getenv("TOKEN")
BOT_USERNAME: Final = '@gromamicon_bot'
print(bot_token)


async def start(update, context):
    await show_description(update, context)
    await show_menu(update, context)


async def show_description(update, context):
    image_url = ('https://pohcdn.com/guide/sites/default/files/styles/paragraph__hero_banner__hb_image__1280bp/public'
                 '/hero_banner/Niagara-falls.jpg')
    caption = 'Hi! Do you like this picture?'

    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('❤️', callback_data='like'), InlineKeyboardButton('👎', callback_data='dislike')],
    ])

    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=image_url, caption=caption, reply_markup=ikb)


async def show_menu(update, context):
    keyboard = [
        [InlineKeyboardButton("Information about place", callback_data='place_info')],
        [InlineKeyboardButton("Visit this place", callback_data='visit')],
        [InlineKeyboardButton("more information", callback_data='contact_info')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Select part menu', reply_markup=reply_markup)


async def button_click(update, context):
    query = update.callback_query
    button = query.data
    await query.answer()

    if button == 'like':
        info_text = "You like this photo"
        await context.bot.send_message(chat_id=query.message.chat_id, text=info_text)

    elif button == 'dislike':
        info_text = "You dont like this photo"
        await context.bot.send_message(chat_id=query.message.chat_id, text=info_text)

    elif button == 'place_info':
        # Отправка информации about place
        info_text = '''Несмотря на то, что Ниагарский водопад находится примерно в 130 км от города Торонто, 
        он считается его главной природной достопримечательностью. Ниагара является одним из самых удивительных и 
        живописных водопадов в мире. Свое начало он берет на территории США, но самые завораживающие виды достались 
        Канаде.'''

        await context.bot.send_message(chat_id=query.message.chat_id, text=info_text)

    elif button == 'visit':
        # send a map for visit this  place
        map_screen = 'C:/Users/konst/Downloads/Screenshot_map_niagara.png'
        # with open(map_screen, 'rb') as file:
        await context.bot.send_photo(chat_id=query.message.chat_id, photo=open(map_screen, "rb"))

    elif button == 'contact_info':
        # Отправка контактной информации
        info_text = """
    Служба Поддержки Клиентов
    Получите помощь с бронированием, изменениями, платежами и технической поддержкой для безупречного опыта.
    Email: support@scantrip.com
    
    Юридический адрес
    Scantrip Inc.
    1000 N. West Street Suite 1200, PMB # 5017
    Wilmington, Delaware,
    19801 USA
        """
        await context.bot.send_message(chat_id=query.message.chat_id, text=info_text)


async def help_command(update: Update, context: CallbackContext):
    help_message = """
    The following commands are available:

    /start -> Hi! Do you like this picture?
    /help -> Command list
    /caps -> Upper message
    """
    await context.bot.send_message(chat_id=update.effective_chat.id, text=help_message)


def main():
    application = ApplicationBuilder().token(bot_token).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('desc', show_description))
    application.add_handler(CommandHandler('menu', show_menu))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CallbackQueryHandler(button_click))

    application.run_polling()


# Вызываем главную функцию
if __name__ == '__main__':
    main()
