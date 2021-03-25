from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

'''фільтри для хендлерів знаходяться в модулі {Filters}'''
message_functions_dict ={'echo': Filters.text & ~Filters.command}

def echo(update: Update, context: CallbackContext) -> None:
    """Ехо-відповідь користувачу"""
    update.message.reply_text(update.message.text)

def echo_with_scenario(update: Update, context: CallbackContext) -> None:
    pass