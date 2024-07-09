import os

from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder,  CommandHandler, CallbackQueryHandler, CallbackContext

load_dotenv()

bot_token = os.getenv("TOKEN")


async def start(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Hi')


async def caps(update: Update, context: CallbackContext):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


async def show_menu(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Информация о колледже", callback_data='college_info')],
        [InlineKeyboardButton("Практика", callback_data='praktika')],
        [InlineKeyboardButton("Контактная информация", callback_data='contact_info')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Выберите пункт меню:', reply_markup=reply_markup)


async def help_command(update: Update, context: CallbackContext):
    help_message = """
    The following commands are available:
    
    /start -> Welcome to the channel
    /help -> This message
    /content -> free of course
    /Python  -> The first video from Python
    /SQL -> The first video from SQL 
    /Java -> The first video from Java
    /Skillup -> Free platform for certification by Simplilearn
    /contact -> contact information 
    """
    await context.bot.send_message(chat_id=update.effective_chat.id, text=help_message)


async def content(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="We have various playlists and articles available!")


async def Python(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Tutorial link : https://www.youtube.com/watch?v=KdZ4HF1SrFs")


async def SQL(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Tutorial link : https://www.youtube.com/watch?v=sLwiFGAOMK4&list=PLqj7-hRTFl_oweCD2cFQYdJDmD5bwEhb9")


async def Java(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Tutorial link : https://www.youtube.com/watch?v=eWk4wrks7qk")


async def Skillup(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Tutorial link : https://stepik.org/lesson/984730/step/2?unit=992009")


async def contact(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="You can contact on the official mail id")


async def handle_message(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"You said {update.message.text}, use the commands using /")


async def button_click(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    if query.data == 'college_info':
        await context.bot.send_message(chat_id=query.message.chat_id, text="Вы выбрали информацию о колледже")
    elif query.data == 'praktika':
        await context.bot.send_message(chat_id=query.message.chat_id, text="Вы выбрали практику")
    elif query.data == 'contact_info':
        await context.bot.send_message(chat_id=query.message.chat_id, text="Вы выбрали контактную информацию")


def main():
    application = ApplicationBuilder().token(bot_token).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('content', content))
    application.add_handler(CommandHandler('Python', Python))
    application.add_handler(CommandHandler('SQL', SQL))
    application.add_handler(CommandHandler('Java', Java))
    application.add_handler(CommandHandler('Skillup', Skillup))
    application.add_handler(CommandHandler('contact', contact))
    application.add_handler(CommandHandler('caps', caps))
    application.add_handler(CommandHandler('menu', show_menu))
    application.add_handler(CallbackQueryHandler(button_click))

    application.run_polling()


if __name__ == '__main__':
    main()
