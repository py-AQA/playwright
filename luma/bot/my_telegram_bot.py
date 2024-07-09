import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

##### Создание общего функционала самого бота                  ####
##### Здесь находиться общие команды которые обрабатывает бот  ####
##### Можно добавить свои обработчики команд                   ####

# bot_token = 'your_bot_token'

bot_token = "7231990870:AAHgudb0N-tDdKcAI8jVc8Wm4ko4135lX0I"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Hi')

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

def main():

    application = ApplicationBuilder().token(bot_token).build()

    start_handler = CommandHandler('start', start)
    caps_handler = CommandHandler('caps', caps)
    application.add_handler(start_handler)
    application.add_handler(caps_handler)

    application.run_polling()

if __name__ == '__main__':
    main()
