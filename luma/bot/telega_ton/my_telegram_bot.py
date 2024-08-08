import html
import json
import logging
import os
import traceback
from typing import Final, Optional

from dotenv import load_dotenv
from telegram import Update, Message
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

load_dotenv()
bot_token = os.getenv("TOKEN")
api_id = os.getenv("APP_ID")
api_hash = os.getenv("APP_HASH")
telethon_session = os.getenv("SESSION_NAME")
BOT_USERNAME: Final = '@gromamicon_bot'
print(telethon_session)
print(api_id)
print(api_hash)

caps_mode = False

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
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


def handle_response(message: Optional[Message]) -> str:
    print(message)
    reply_sms = ""
    message_type: str = message.chat.type
    text: str = message.text
    processed: str = text.lower()
    print(f'User({message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            reply_sms: str = text.replace(BOT_USERNAME, '').strip()
    else:
        reply_sms: str = text

    if "hello" in processed:
        reply_sms = "Hey There"

    if "how are you" in processed:
        reply_sms = "I am good"

    if "i like python" in processed:
        reply_sms = "Its Cool!"
    return reply_sms


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_sms = handle_response(update.message)

    if caps_mode:
        text_sms = text_sms.upper()
    else:
        text_sms = text_sms.lower()

    print('Bot:', text_sms)
    await update.message.reply_text(text_sms)


async def selector_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "/caps":
        await caps(update, context)
    elif update.message.text == "/stop_caps":
        await stop_caps(update, context)
    else:
        await handle_message(update, context)


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log the error and send a telegram message to notify the developer."""
    # Log the error before we do anything else, so we can see it even if something breaks.
    logger.error("Exception while handling an update:", exc_info=context.error)

    # traceback.format_exception returns the usual python message about an exception, but as a
    # list of strings rather than a single string, so we have to join them together.
    tb_list = traceback.format_exception(None, context.error, context.error.__traceback__)
    tb_string = "".join(tb_list)

    # Build the message with some markup and additional information about what happened.
    # You might need to add some logic to deal with messages longer than the 4096 character limit.
    update_str = update.to_dict() if isinstance(update, Update) else str(update)
    message = (
        "An exception was raised while handling an update\n"
        f"<pre>update = {html.escape(json.dumps(update_str, indent=2, ensure_ascii=False))}"
        "</pre>\n\n"
        f"<pre>context.chat_data = {html.escape(str(context.chat_data))}</pre>\n\n"
        f"<pre>context.user_data = {html.escape(str(context.user_data))}</pre>\n\n"
        f"<pre>{html.escape(tb_string)}</pre>"
    )

    # Finally, send the message
    await context.bot.send_message(
        chat_id=api_id, text=message, parse_mode=ParseMode.HTML
    )


def main():
    application = ApplicationBuilder().token(bot_token).build()
    # My Command
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('caps', caps))
    application.add_handler(CommandHandler("custom", custom_command))
    # My Message
    application.add_handler(MessageHandler(filters.TEXT, selector_handler))
    application.add_error_handler(error_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
