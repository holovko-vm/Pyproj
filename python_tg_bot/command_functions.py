from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import re

regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

command_functions_list = ['kill', 'commands', 'registration', 'out']


def commands(**kwargs):
    def commands(update: Update, context: CallbackContext) -> None:
        """Повертає список використовуваних ботом команд"""
        update.message.reply_text(
            f'Список доступних команд - {command_functions_list}')
    return commands


def kill(**kwargs):
    def kill(update: Update, context: CallbackContext) -> None:
        """Фан-функція, формат виклику /kill 'name' """
        if len(update.message.text) <= 6:
            update.message.reply_text('Nobody to kill')
        else:
            update.message.reply_text(
                f'We will kill {update.message.text[6:]} for you')
    return kill

    user_state = 0


def registration(users_ctx, **kwargs):

    def registration(update: Update, context: CallbackContext) -> None:
        users_ctx['user_state'] = 1
        update.message.reply_text('Процедуру реєстрації запущено,'+
        'для виходу з реєстрації, скористайтесь командою /out')
        update.message.reply_text('Для продовження реєстрації введіть email')
    return registration

def out(users_ctx, **kwargs):

    def out(update: Update, context: CallbackContext) -> None:
        users_ctx['user_state'] = 0
        update.message.reply_text('Реєстрацію відмінено!')
    return out