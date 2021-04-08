from command_functions import command_functions_list
from message_functions import message_functions_dict
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
        self.users_ctx = {'user_state': 0}
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

    # def add_message_handlers(self, message_handlers=None):
    #     for message_function, filter in message_handlers.items():
    #         try:
    #             self.dispatcher.\
    #                 add_handler(MessageHandler(filter, getattr(
    #                     message_functions, message_function)(users_ctx=self.users_ctx)
    #                 ))
    #         except AttributeError:
    #             logging.error(
    #                 f'Невідома функція - {message_function}, додайте її до файлу bot_commands.py')

    def add_message_handlers(self, message_handlers=None):
        for message_function, filter in message_handlers.items():
            try:
                self.dispatcher.\
                    add_handler(MessageHandler(filter, getattr(
                        message_functions, message_function)(users_ctx=self.users_ctx)
                    ))
            except AttributeError:
                logging.error(
                    f'Невідома функція - {message_function}, додайте її до файлу bot_commands.py')

    def run(self, command_handlers=None, message_handlers=None):
        """Створюємо обробників"""
        self.add_message_handlers(message_handlers)
        self.add_command_handlers(command_handlers)
        """Слухаємо сервер"""
        self.updater.start_polling()
        self.updater.idle()