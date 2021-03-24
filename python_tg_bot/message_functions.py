from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

message_functions_list =['echo']

def echo(update: Update, context: CallbackContext) -> None:
    """Ехо-відповідь користувачу"""
    update.message.reply_text(update.message.text)
