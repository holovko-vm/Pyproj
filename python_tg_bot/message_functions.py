from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import re
import pymysql.cursors

def user_message_handler(users_ctx, **kwargs):
    re_email = re.compile('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$')
    re_url = re.compile(r"((https?):((//)|(\\\\))+[\w\d:#@%/;$()~_?\+-=\\\.&]*)")
    def user_message_handler(update=Update, context=CallbackContext,
     users_ctx=users_ctx, re_email=re_email, *args, **kwargs):
        users_ctx['user_state'][update.message.from_user['id']] = 0
        if users_ctx['user_handler']==1:
            echo(update=update, context=context)
        if users_ctx['user_handler']==0:
            echo_for_meeting(users_ctx, update, context, re_email)

    return user_message_handler

def echo(update,context):
    """Ехо-відповідь користувачу"""
    return update.message.reply_text(update.message.text)

def echo_for_meeting(users_ctx, update: Update, context: CallbackContext, re_email) -> None:
    print(users_ctx['user_state'][update.message.from_user['id']])
    if users_ctx['user_state']['user'] == 0:
        _date = '15 квітня'
        _time = '10 ранку'
        _location = 'Виставковому центрі, павільйон 1А'
        _INTENT = [
            {'name': 'Дата проведення',
                'tokens': ('коли', "котра", "о котрій", "дат"),
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
    if users_ctx['user_state']['user'] == 1:
        if re_email.search(update.message.text):
            print(users_ctx['user_state'][update.message.from_user['id']])
            users_ctx['user_email']= update.message.text
            users_ctx['user_state']['user'] = 2
            users_ctx['user_state'][update.message.from_user['id']] = 1
            return update.message.reply_text('Введіть password')
        else:
            users_ctx['user_state']['user'] = 1
            print(users_ctx['user_state'][update.message.from_user['id']])
            users_ctx['user_state'][update.message.from_user['id']]=2
            return update.message.reply_text('Введіть коректний email')
    elif users_ctx['user_state']['user'] == 2:
        if len(update.message.text) >= 8:
            users_ctx['probe_pass'] = update.message.text
            users_ctx['user_state']['user'] = 3
            print(users_ctx['user_state'][update.message.from_user['id']])
            users_ctx['user_state'][update.message.from_user['id']]=4
            return update.message.reply_text('Підтвердіть password')
        else:
            return update.message.reply_text('Пароль повинен бути більше 8 літер')
    elif users_ctx['user_state']['user'] == 3:
        if update.message.text == users_ctx['probe_pass']:
            users_ctx['password'] = update.message.text
            connection = pymysql.connect(host='localhost',
                             user='root',
                             password='19951977',
                             database='mypythondata',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
# update.message.from_user['id']
            with connection:
                with connection.cursor() as cursor:
                    sql = "INSERT INTO `registration_info` (`user_email`, `user_password`, `user_state`) VALUES (%s, %s, %s)"
                    cursor.execute(sql, (users_ctx['user_email'], users_ctx['password'], 0))
                connection.commit()
            users_ctx['user_state']['user'] = 0
            print(users_ctx['user_state'][update.message.from_user['id']])
            users_ctx['user_state'][update.message.from_user['id']] =5
            return update.message.reply_text('Реєстрація успішна!')
        else:
            users_ctx['user_state']['user'] = 2
            return update.message.reply_text(
                'Некоректний повторний пароль.\nВведіть password')