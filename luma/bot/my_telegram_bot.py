import logging
from typing import Final

from dotenv import dotenv_values
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

settings: dict = dotenv_values(".env")
bot_token = settings.get("TOKEN")
BOT_USERNAME: Final = '@gromamicon_bot'
caps_mode = False


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.warning(context)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! Thank you for chatting with me!")


async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global caps_mode
    caps_mode = True
    await update.message.reply_text("Caps mode is ON!")
    # text = update.message.text
    # await update.message.reply_text(text.upper())


async def stop_caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global caps_mode
    caps_mode = False
    await update.message.reply_text("Caps mode is OFF!")


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="This is custom command!")


def handle_response(text: str) -> str:
    processed: str = text.lower()

    if "hello" in processed:
        return "Hey There"

    if "how are you" in processed:
        return "i am good"

    if "i love python" in processed:
        return "Its Cool!"

    return "I dont understand what you wrote"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(f'User({update.message.chat.id}) in {message_type}: "{text}"')

    if caps_mode:
        text = text.upper()
    else:
        text = text.lower()

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    if response == handle_response(text):
        print('Bot:', response)
        await update.message.reply_text(response)

    if response != handle_response(text):
        print('Bot:', text)
    await update.message.reply_text(text)


async def selector_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "/caps":
        await caps(update, context)
    elif update.message.text == "/stop_caps":
        await stop_caps(update, context)
    else:
        await handle_message(update, context)


def error(bot, update, error):
    logging.warning('Update "%s" caused error "%s"' % (update, error))


def main():
    application = ApplicationBuilder().token(bot_token).build()
    # My Command
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('caps', caps))
    application.add_handler(CommandHandler("custom", custom_command))
    # My Message
    application.add_handler(MessageHandler(filters.TEXT, selector_handler))
    application.add_error_handler()
    application.run_polling()


if __name__ == '__main__':
    main()
