from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackContext


def echo(update: Update, context: CallbackContext) -> None:
    """Ехо-відповідь користувачу"""
    update.message.reply_text(update.message.text)
