from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import re

regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

command_functions_list =['kill','commands']
def commands(update: Update, context: CallbackContext) -> None:
    """Повертає список використовуваних ботом команд"""
    update.message.reply_text(f'Список доступних команд - {command_functions_list}')


def kill(update: Update, context: CallbackContext) -> None:
    """Фан-функція, формат виклику /kill 'name' """
    if len(update.message.text) <= 6:
        update.message.reply_text('Nobody to kill')
    else:
        update.message.reply_text(
            f'We will kill {update.message.text[6:]} for you')

def registration(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Введіть email')
    user_email = update.message.text
    if re.search(regex, user_email):
        update.message.reply_text('Введіть password')
        message1 = update.message.text
        update.message.reply_text('Підтвердіть password')       
        if update.message.text == message1:
            update.message.text = password
            update.message.reply_text('Реєстрація успішна!')
            with open('data_base.txt', 'a', 'utf-8') as file:
                file.write(f'{user_email} : {password},')
                