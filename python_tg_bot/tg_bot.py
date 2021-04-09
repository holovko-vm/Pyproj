from command_functions import command_functions_list
import message_functions
import command_functions
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


"""Список використовуваних ботом функцій """
'''message_functions_dict, command_functions_list'''


class My_tg_bot:
    def __init__(self, token):
        """Створюємо Об'єкт, що слідкує за новинами,
        Вставте токен Вашого бота token_bot.py.default --> token_bot.py >>token = 'Токен Вашого бота'
        """
        self.updater = Updater(token=token)
        """Створюємо Об'єкт, який направляє новину відповідному обробнику"""
        self.dispatcher = self.updater.dispatcher
        self.users_ctx = {'user_state': 0, 'user_handler':0}
# TODO прописати стейти для кожного користувача по його ід
    
    def add_command_handlers(self, commands=None):
        """Метод створення обробників згідно списку команд з COMMAND_LIST"""
        for command in commands:
            try:
                self.dispatcher.add_handler(CommandHandler(
                    command, getattr(command_functions, command)(users_ctx=self.users_ctx)))
            except AttributeError:
                logging.error(
                    f'Невідома функція - {command}, додайте її до файлу bot_commands.py')

    def add_message_handlers(self):
        '''фільтри для хендлерів знаходяться в модулі {Filters}'''
        filter = Filters.text & ~Filters.command
        try:
            self.dispatcher.\
                add_handler(MessageHandler\
                    (filter, message_functions.user_message_handler(users_ctx=self.users_ctx)))
        except Exception as ecx:
            logging.error(f'Помилка -{ecx}')

    def run(self, command_handlers=None):
        """Створюємо обробників"""
        self.add_message_handlers()
        self.add_command_handlers(command_handlers)
        """Слухаємо сервер"""
        self.updater.start_polling()
        self.updater.idle()


