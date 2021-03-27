from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import re

'''фільтри для хендлерів знаходяться в модулі {Filters}'''
message_functions_dict = {'echo_regist': Filters.text & ~Filters.command}


def echo(update: Update, context: CallbackContext) -> None:
    """Ехо-відповідь користувачу"""
    update.message.reply_text(update.message.text)


def echo_for_meeting(update: Update, context: CallbackContext) -> None:
    _date = '15 квітня'
    _time = '10 ранку'
    _location = 'Виставковому центрі, павільйон 1А'
    _INTENT = [
        {'name': 'Дата проведення',
         'tokens': ('коли', "котра", "о котрій", "дату", "дата"),
         'answer': f'Конференція відбудеться {_date}, регістрація починається о {_time}'
         },
        {'name': 'Місце проведення',
         'tokens': ('де', "місце", "локація", "метро", "адрес"),
         'answer': f'Конференція проводиться в {_location}'
         },
    ]
    DEFAULT_ANSWER = 'Поки не знаю як Вам відповісти, але я можу відповісти на питання де і коли відбудеться виставка'
    for _ in _INTENT:
        for token in _['tokens']:
            if token in str.lower(update.message.text):
                update.message.reply_text(_['answer'])
                return
    else:
        update.message.reply_text(DEFAULT_ANSWER)


def echo_regist():
    user_state = 0
    probe_pass = None
    password = None
    user_email = None
    re_email = re.compile('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$')

    def echo_regist_1(update: Update, context: CallbackContext) -> None:
        nonlocal user_state, probe_pass, password, user_email

        if user_state == 0:
            user_email = update.message.text
            if re_email.search(user_email):
                user_state = 2
                update.message.reply_text('Введіть password')
            else:
                user_state = 0
                update.message.reply_text('Введіть email')

        elif user_state == 2:
            if len(update.message.text) >= 8:
                update.message.reply_text('Підтвердіть password')
                probe_pass = update.message.text
                user_state = 3
            else:
                update.message.reply_text('Пароль повинен бути більше 8 літер')
        elif user_state == 3:
            if update.message.text == probe_pass:
                password = update.message.text
                update.message.reply_text('Реєстрація успішна!')
                with open(file='python_tg_bot\\data_base.txt', mode='a', encoding='utf-8') as file:
                    file.write(f'{user_email} : {password},')
                user_state = 4
            else:
                update.message.reply_text(
                    'Некоректний повторний пароль.\nВведіть password')
                user_state = 2

    return echo_regist_1
