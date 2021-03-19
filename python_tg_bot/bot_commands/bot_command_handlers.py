from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackContext


def echo(update: Update, context: CallbackContext) -> None:
    """Ехо-відповідь користувачу"""
    update.message.reply_text(update.message.text)


def commands(update: Update, context: CallbackContext) -> None:
    """Повертає список використовуваних ботом команд"""
    update.message.reply_text(f'Список доступних команд - {COMMAND_LIST}')


def kill(update: Update, context: CallbackContext) -> None:
    """Фан-функція, формат виклику /kill 'name' """
    if len(update.message.text) <= 6:
        update.message.reply_text('Nobody to kill')
    else:
        update.message.reply_text(
            f'We will kill {update.message.text[6:]} for you')