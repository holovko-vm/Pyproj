from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import re
import requests
from bs4 import BeautifulSoup

regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

command_functions_list = ['kill', 'commands', 'registration', 'out','switch', 'weather']


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

    def registration(update: Update, context: CallbackContext) -> None:
        users_ctx['user_state'] = 1
        update.message.reply_text('Процедуру реєстрації запущено,'+
        'для виходу з реєстрації, скористайтесь командою /out')
        update.message.reply_text('Для продовження реєстрації введіть email')
    return registration

def out(users_ctx, **kwargs):

    def out(update: Update, context: CallbackContext) -> None:
        users_ctx['user_state'] = 0
        update.message.reply_text('Реєстрацію відмінено!')
    return out


def switch(users_ctx, **kwargs):

    def switch(update: Update, context: CallbackContext) -> None:
        if users_ctx['user_handler'] == 1:
            users_ctx['user_handler'] = 0
            update.message.reply_text('перемкнулось')
            return
        users_ctx['user_handler'] = 1
        update.message.reply_text('перемкнулось')
    return switch

def weather(users_ctx, **kwargs):

    def weather(update: Update, context: CallbackContext) -> None:
        response = requests.get('https://www.wunderground.com/weather/IKYIV366')
        if response.status_code ==200:
            html_doc = BeautifulSoup(response.text, features='html.parser')
            list_of = html_doc.find_all('span', {'class':'wu-value wu-value-to'})
            i=0
            for tag in list_of:
                i+=1
                if i == 2:
                    tag = str(tag)
                    value = int(tag[-9:-7])
                    gradus = (value - 32)/1.8
                    real_gradus = round(gradus, 1)
                    update.message.reply_text(f'Температура у Києві - {real_gradus} °C')
                    # TODO присилати якість погоди окрім градусів
            
    return weather