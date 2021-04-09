from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import re

'''фільтри для хендлерів знаходяться в модулі {Filters}'''
message_functions_dict = {'user_message_handler': Filters.text & ~Filters.command}

def echo(update,context,givno):
    """Ехо-відповідь користувачу"""
    return update.message.reply_text(update.message.text)
def echo_2(update,context):
    """Ехо-відповідь користувачу"""
    return update.message.reply_text('ха-ха бидлокод, моя взяла')
    
def user_message_handler(users_ctx, **kwargs):
    
    password = None
    user_email = None
    probe_pass = None
    def user_message_handler(update=Update, context=CallbackContext,
     users_ctx=users_ctx, probe_pass=probe_pass, *args, **kwargs):
        
        print('start')
        print(f'start users_ctx - {users_ctx}')
        if users_ctx['user_handler']==1:
            echo(update=update, context=context, givno=1)
        if users_ctx['user_handler']==0:
            nonlocal password, user_email
            print(f'до виклику пас такий - {probe_pass}')
            echo_for_meeting(users_ctx, probe_pass, password, user_email, update, context)
        print(f'після виклику пас такий - {probe_pass}')
        print(f'end users_ctx - {users_ctx}')
        print('end')
    return user_message_handler


    

    
def echo_for_meeting(users_ctx, probe_pass, password, user_email, update: Update, context: CallbackContext) -> None:
    re_email = re.compile('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$')
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

    # nonlocal probe_pass, password, user_email
    if users_ctx['user_state'] == 1:
        user_email = update.message.text
        if re_email.search(user_email):
            users_ctx['user_state'] = 2
            return update.message.reply_text('Введіть password')
        else:
            users_ctx['user_state'] = 1
            return update.message.reply_text('Введіть коректний email')
    elif users_ctx['user_state'] == 2:
        if len(update.message.text) >= 8:
            probe_pass = update.message.text
            users_ctx['user_state'] = 3
            return probe_pass, update.message.reply_text('Підтвердіть password')
        else:
            return update.message.reply_text('Пароль повинен бути більше 8 літер')
    elif users_ctx['user_state'] == 3:
        if update.message.text == probe_pass:
            password = update.message.text
            print('Попав у блок реєстрації, проб-пас нарешті замкнувся')
            with open(file='python_tg_bot\\data_base.txt', mode='a', encoding='utf-8') as file:
                file.write(f'{user_email} : {password},')
                print('Запис вдався')
            users_ctx['user_state'] = 0
            print('невже!!!!')
            return update.message.reply_text('Реєстрація успішна!')
        else:
            users_ctx['user_state'] = 2
            return update.message.reply_text(
                'Некоректний повторний пароль.\nВведіть password')
         





# def echo_for_meeting(users_ctx, **kwargs):
#     probe_pass = None
#     password = None
#     user_email = None
#     re_email = re.compile('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$')

#     def echo_for_meeting(update: Update, context: CallbackContext) -> None:
#         if users_ctx['user_state'] == 0:
#             _date = '15 квітня'
#             _time = '10 ранку'
#             _location = 'Виставковому центрі, павільйон 1А'
#             _INTENT = [
#                 {'name': 'Дата проведення',
#                  'tokens': ('коли', "котра", "о котрій", "дату", "дата"),
#                  'answer': f'Конференція відбудеться {_date}, регістрація починається о {_time}'
#                  },
#                 {'name': 'Місце проведення',
#                  'tokens': ('де', "місце", "локація", "метро", "адрес"),
#                  'answer': f'Конференція проводиться в {_location}'
#                  },
#             ]
#             DEFAULT_ANSWER = 'Поки не знаю як Вам відповісти, але я можу відповісти на питання де і коли відбудеться виставка'
#             for _ in _INTENT:
#                 for token in _['tokens']:
#                     if token in str.lower(update.message.text):
#                         update.message.reply_text(_['answer'])
#                         return
#             else:
#                 update.message.reply_text(DEFAULT_ANSWER)

#         nonlocal probe_pass, password, user_email
#         if users_ctx['user_state'] == 1:
#             user_email = update.message.text
#             if re_email.search(user_email):
#                 users_ctx['user_state'] = 2
#                 update.message.reply_text('Введіть password')
#             else:
#                 users_ctx['user_state'] = 1
#                 update.message.reply_text('Введіть коректний email')

#         elif users_ctx['user_state'] == 2:
#             if len(update.message.text) >= 8:
#                 update.message.reply_text('Підтвердіть password')
#                 probe_pass = update.message.text
#                 users_ctx['user_state'] = 3
#             else:
#                 update.message.reply_text('Пароль повинен бути більше 8 літер')
#         elif users_ctx['user_state'] == 3:
#             if update.message.text == probe_pass:
#                 password = update.message.text
#                 update.message.reply_text('Реєстрація успішна!')
#                 with open(file='python_tg_bot\\data_base.txt', mode='a', encoding='utf-8') as file:
#                     file.write(f'{user_email} : {password},')
#                 users_ctx['user_state'] = 0
#             else:
#                 update.message.reply_text(
#                     'Некоректний повторний пароль.\nВведіть password')
#                 users_ctx['user_state'] = 2
#     return echo_for_meeting
