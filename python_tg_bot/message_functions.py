from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import re

def user_message_handler(users_ctx, **kwargs):
    re_email = re.compile('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$')
    def user_message_handler(update=Update, context=CallbackContext,
     users_ctx=users_ctx, re_email=re_email, *args, **kwargs):
        if users_ctx['user_handler']==1:
            echo(update=update, context=context)
        if users_ctx['user_handler']==0:
            echo_for_meeting(users_ctx, update, context, re_email)
    return user_message_handler

def echo(update,context):
    """Ехо-відповідь користувачу"""
    return update.message.reply_text(update.message.text)

def echo_for_meeting(users_ctx, update: Update, context: CallbackContext, re_email) -> None:
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
                    return update.message.reply_text(_['answer'])          
        else:
            return update.message.reply_text(DEFAULT_ANSWER)
    if users_ctx['user_state'] == 1:
        if re_email.search(update.message.text):
            users_ctx['user_email']= update.message.text
            users_ctx['user_state'] = 2
            return update.message.reply_text('Введіть password')
        else:
            users_ctx['user_state'] = 1
            return update.message.reply_text('Введіть коректний email')
    elif users_ctx['user_state'] == 2:
        if len(update.message.text) >= 8:
            users_ctx['probe_pass'] = update.message.text
            users_ctx['user_state'] = 3
            return update.message.reply_text('Підтвердіть password')
        else:
            return update.message.reply_text('Пароль повинен бути більше 8 літер')
    elif users_ctx['user_state'] == 3:
        if update.message.text == users_ctx['probe_pass']:
            users_ctx['password'] = update.message.text
            with open(file='python_tg_bot\\data_base.txt', mode='a', encoding='utf-8') as file:
                for key, item in users_ctx.items():
                    if key == 'user_email':
                        file.write(item)
                        file.write(' : ')
                    if key == 'password':
                        file.write(item)
                        file.write(' , ')
            users_ctx['user_state'] = 0
            return update.message.reply_text('Реєстрація успішна!')
        else:
            users_ctx['user_state'] = 2
            return update.message.reply_text(
                'Некоректний повторний пароль.\nВведіть password')