from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

'''фільтри для хендлерів знаходяться в модулі {Filters}'''
message_functions_dict ={'echo_for_meeting': Filters.text & ~Filters.command}

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