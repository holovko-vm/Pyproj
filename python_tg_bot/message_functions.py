from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import re
import pymysql.cursors
from settings import database
import logging

def user_message_handler(users_ctx, **kwargs):
    """Обробник повідомлень, визначає функції, 
    що використовуються для обробки повідомлень та умови, за яких вони обираються"""
    re_email = re.compile('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$')
    re_url = re.compile(r"((https?):((//)|(\\\\))+[\w\d:#@%/;$()~_?\+-=\\\.&]*)")
    def user_message_handler(update=Update, context=CallbackContext,
     users_ctx=users_ctx, re_email=re_email, *args, **kwargs):
        try:
            connection = pymysql.connect(host=database['host'],
                                user=database['user'],
                                password=database['password'],
                                database=database['database'],
                                charset=database['charset'],
                                cursorclass=pymysql.cursors.DictCursor)
        except Exception as ecx:
            logging.error(f'No database - {ecx}')
            
        try:
            """Оскільки при запуску бота невідомо, від якого користувача надійде повідомлення, 
            цей блок відповідає за створення контексту конкретного користувача в частині обробника користувача"""
            if users_ctx['user_handler'][update.message.from_user['id']]:
                pass
        except KeyError:
            users_ctx['user_handler'][update.message.from_user['id']]=0 

        """Умови для вибору функції обробки повідомлень, задаються тут"""   
        if users_ctx['user_handler'][update.message.from_user['id']]==0:
            echo_for_meeting(users_ctx, update, context, re_email, connection)     
        if users_ctx['user_handler'][update.message.from_user['id']]==1:
            echo(update=update, context=context)
        

    return user_message_handler

def echo(update,context):
    """Ехо-відповідь користувачу"""
    return update.message.reply_text(update.message.text)

def echo_for_meeting(users_ctx, update: Update, context: CallbackContext, re_email, connection) -> None:
    """Функція для організації івенту, надання інформації та реєстрації"""
    try:
        """Оскільки при запуску бота невідомо, від якого користувача надійде повідомлення, 
            цей блок відповідає за створення контексту конкретного користувача 
            в частині стану проходження сценарію користувача"""
        if users_ctx['user_state'][update.message.from_user['id']]:
            pass
    except KeyError:
        users_ctx['user_state'][update.message.from_user['id']] = 0
        
    if users_ctx['user_state'][update.message.from_user['id']] == 0:
        """Базові відповіді користувачу"""
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
        
        
        
    if users_ctx['user_state'][update.message.from_user['id']] == 1:
        """Сценарій реєстрації, запускається за допомогою команди /registration"""
        if re_email.search(update.message.text):
            users_ctx['user_email']= update.message.text
            users_ctx['user_state'][update.message.from_user['id']] = 2
            return update.message.reply_text('Введіть password')
        else:
            users_ctx['user_state'][update.message.from_user['id']]=1
            return update.message.reply_text('Введіть коректний email')
        
    elif users_ctx['user_state'][update.message.from_user['id']] == 2:
        if len(update.message.text) >= 8:
            users_ctx['probe_pass'] = update.message.text
            users_ctx['user_state'][update.message.from_user['id']]=3
            return update.message.reply_text('Підтвердіть password')
        else:
            return update.message.reply_text('Пароль повинен бути більше 8 літер')
        
    elif users_ctx['user_state'][update.message.from_user['id']] == 3:
        if update.message.text == users_ctx['probe_pass']:
            users_ctx['password'] = update.message.text
            users_ctx['user_state'][update.message.from_user['id']] = 0
            with connection:
                with connection.cursor() as cursor:
                    table = "CREATE TABLE IF NOT EXISTS `registration_info`(user_id INT PRIMARY KEY NOT NULL, user_email VARCHAR(30) NOT NULL, user_password VARCHAR(30) NOT NULL)"
                    cursor.execute(table)
                    reg = "REPLACE INTO `registration_info` (`user_id`,`user_email`, `user_password`) VALUES (%s,%s, %s)"
                    cursor.execute(reg, (update.message.from_user['id'],users_ctx['user_email'], users_ctx['password']))
                connection.commit()
            return update.message.reply_text('Реєстрація успішна!')
        else:
            users_ctx['user_state'][update.message.from_user['id']] = 2
            return update.message.reply_text(
                'Некоректний повторний пароль.\nВведіть password')