from os.path import join
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests
from bs4 import BeautifulSoup


"""Список використовуваних ботом команд"""
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



def registration(users_ctx, **kwargs):
    """Запускає сценарій реєстрації"""
    def registration(update: Update, context: CallbackContext) -> None:
        users_ctx['user_handler'][update.message.from_user['id']] = 0
        users_ctx['user_state'][update.message.from_user['id']] = 1
        update.message.reply_text('Процедуру реєстрації запущено,'+
        'для виходу з реєстрації, скористайтесь командою /out')
        update.message.reply_text('Для продовження реєстрації введіть email')
    return registration

def out(users_ctx, **kwargs):
    """Команда для виходу з процесу реєстрації"""
    def out(update: Update, context: CallbackContext) -> None:
        users_ctx['user_state'][update.message.from_user['id']] = 0
        update.message.reply_text('Реєстрацію відмінено!')
    return out


def switch(users_ctx, **kwargs):
    """Команда для зміни функції обробки повідомлень"""
    def switch(update: Update, context: CallbackContext) -> None:
        try:
            if users_ctx['user_handler'][update.message.from_user['id']]:
                pass
        except KeyError:
            users_ctx['user_handler'][update.message.from_user['id']]=0
        if users_ctx['user_handler'][update.message.from_user['id']] == 1:
            users_ctx['user_handler'][update.message.from_user['id']] = 0
            update.message.reply_text('Використовується інша функція обробки повідомлень')
            return
        users_ctx['user_handler'][update.message.from_user['id']] = 1
        update.message.reply_text('Використовується інша функція обробки повідомлень')
    return switch

def weather(users_ctx, **kwargs):
    """Команда для отримання поточної погоди у Києві"""
    def weather(update: Update, context: CallbackContext) -> None:
        response = requests.get('https://www.wunderground.com/weather/IKYIV366')
        if response.status_code ==200:
            html_doc = BeautifulSoup(response.text, features='html.parser')
            list_of_temperature = html_doc.find_all('span', {'class':'wu-value wu-value-to'})
            list_of_weather = html_doc.find_all('img', {'alt':'icon'})
            tag_1=list_of_temperature[1]
            value =int(tag_1.get_text())
            gradus = (value - 32)/1.8
            real_gradus = round(gradus, 1)
            tag_2 = list_of_weather[1]
            link =tag_2.attrs['src']
            img = requests.get("http://www.wunderground.com/static/i/c/v4/33.svg")
            img_file = open('python_tg_bot\\img.svg','wb')
            img_file.write(img.content)
            img_file.close()   
            try:
                import pyvips
                image_weather_prev = join('python_tg_bot','img.svg')
                image_weather_out = join('python_tg_bot','weather.png')
                image = pyvips.Image.thumbnail(image_weather_prev, 75, height=75)
                image.write_to_file(image_weather_out)
                image_weather = open(join('python_tg_bot','weather.png'),"rb")
                update.message.reply_photo(photo=image_weather)
            except Exception:
                image_weather_fault = open(join('python_tg_bot','img.svg'),"rb")
                update.message.reply_document(document=image_weather_fault)
                update.message.reply_text('Lest install pyvips, if you want to see photo')
            update.message.reply_text(f'Температура у Києві : {real_gradus} °C')
             
    return weather