from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import re

regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

command_functions_list = ['kill', 'commands', 'registration']


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
    users_ctx['user_state'] = 1
    probe_pass = None
    password = None
    user_email = None
    re_email = re.compile('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$')

    def echo_regist_1(update: Update, context: CallbackContext) -> None:
        nonlocal probe_pass, password, user_email
        print("text ", update.message.text)
        if users_ctx['user_state'] == 1:
            user_email = update.message.text
            if re_email.search(user_email):
                users_ctx['user_state'] = 2
                update.message.reply_text('Введіть password')
            else:
                users_ctx['user_state'] = 1
                update.message.reply_text('Введіть email')

        elif users_ctx['user_state'] == 2:
            if len(update.message.text) >= 8:
                update.message.reply_text('Підтвердіть password')
                probe_pass = update.message.text
                users_ctx['user_state'] = 3
            else:
                update.message.reply_text('Пароль повинен бути більше 8 літер')
        elif users_ctx['user_state'] == 3:
            if update.message.text == probe_pass:
                password = update.message.text
                update.message.reply_text('Реєстрація успішна!')
                with open(file='python_tg_bot\\data_base.txt', mode='a', encoding='utf-8') as file:
                    file.write(f'{user_email} : {password},')
                users_ctx['user_state'] = 0
            else:
                update.message.reply_text(
                    'Некоректний повторний пароль.\nВведіть password')
                users_ctx['user_state'] = 2

    return echo_regist_1
