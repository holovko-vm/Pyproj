from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import re

'''фільтри для хендлерів знаходяться в модулі {Filters}'''
message_functions_dict = {'echo_for_meeting': Filters.text & ~Filters.command}


def echo(update: Update, context: CallbackContext) -> None:
    """Ехо-відповідь користувачу"""
    update.message.reply_text(update.message.text)


def echo_for_meeting(users_ctx, **kwargs):
    probe_pass = None
    password = None
    user_email = None
    re_email = re.compile('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$')

    def echo_for_meeting(update: Update, context: CallbackContext) -> None:
        if users_ctx['user_state'] == 0:
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

        nonlocal probe_pass, password, user_email
        if users_ctx['user_state'] == 1:
            user_email = update.message.text
            if re_email.search(user_email):
                users_ctx['user_state'] = 2
                update.message.reply_text('Введіть password')
            else:
                users_ctx['user_state'] = 1
                update.message.reply_text('Введіть коректний email')

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
    return echo_for_meeting
