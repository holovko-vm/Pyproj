from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import re

'''фільтри для хендлерів знаходяться в модулі {Filters}'''
message_functions_dict ={'echo_regist': Filters.text & ~Filters.command}

def echo(update: Update, context: CallbackContext) -> None:
    """Ехо-відповідь користувачу"""
    update.message.reply_text(update.message.text)

def echo_for_meeting(update: Update, context: CallbackContext) -> None:
    _date = '15 квітня'
    _time = '10 ранку'
    _location = 'Виставковому центрі, павільйон 1А'
    _INTENT = [
        {'name': 'Дата проведення',
        'tokens': ('коли', "котра","о котрій","дату","дата"),
        'answer': f'Конференція відбудеться {_date}, регістрація починається о {_time}'
        },
        {'name': 'Місце проведення',
        'tokens': ('де', "місце","локація","метро","адрес"), 
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
     
def echo_regist(update: Update, context: CallbackContext) -> None:
    user_state = 0
    print(f'{user_state}'*5)
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if user_state == 0:
        update.message.reply_text('Введіть email')
        user_state = 1
        user_email = update.message.text
        print(user_email)
        if re.search(regex, user_email):
            user_state = 2
        else:
            user_state = 0
        print(f'{user_state}')
    print(f'{user_state}'*10)
    if user_state == 2:
        update.message.reply_text('Введіть password')
        if len(update.message.text)>=8:
            update.message.text = probe_pass
            update.message.text = None
            user_state = 3
    if user_state == 4:       
        update.message.reply_text('Підтвердіть password')       
        if update.message.text == probe_pass:
            update.message.text = password
            update.message.reply_text('Реєстрація успішна!')
            with open(file='python_tg_bot\\data_base.txt', mode='a', encoding='utf-8') as file:
                file.write(f'{user_email} : {password},')
            
                