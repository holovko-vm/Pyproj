from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

'''фільтри для хендлерів знаходяться в модулі {Filters}'''
message_functions_dict ={'echo_for_meeting': Filters.text & ~Filters.command}

def echo(update: Update, context: CallbackContext) -> None:
    """Ехо-відповідь користувачу"""
    update.message.reply_text(update.message.text)

def echo_for_meeting(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'{update.message.text} + ти рак')
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