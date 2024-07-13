from typing import Final

from dotenv import dotenv_values
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

##### Создание общего функционала самого бота                  ####
##### Здесь находиться общие команды которые обрабатывает бот  ####
##### Можно добавить свои обработчики команд                   ####


settings: dict = dotenv_values(".env")
bot_token = settings.get("TOKEN")
BOT_USERNAME: Final = '@gromamicon_bot'


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! Thank you for chatting with me!")


async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # message_type: str = update.message.chat.type
    # text: str = update.message.text
    # text_caps = text.join(context.args).upper()
    # await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)
    # print(f'User({update.message.chat.id}) in {message_type}: "{text}"')

    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

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

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)

    # вызывает ошибку - бот не отвечает в телеге, но в пайчарм в начале сообщения-фейл есть правильный ответ бота
    # await context.bot.send_message(update.message.reply_text(response))
    await update.message.reply_text(response)


def main():
    application = ApplicationBuilder().token(bot_token).build()
    # My Command
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('caps', caps))
    application.add_handler(CommandHandler("custom", custom_command))
    # My Message
    application.add_handler(MessageHandler(filters.TEXT, handle_message))

    application.run_polling()


if __name__ == '__main__':
    main()
