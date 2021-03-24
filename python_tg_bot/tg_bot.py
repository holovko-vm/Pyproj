import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from token_bot import token
import command_functions
import message_functions
from message_functions import message_functions_list
from command_functions import command_functions_list

"""Додаємо логування"""
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d.%m.%Y %I:%M',
    level=logging.INFO,
    handlers=[logging.FileHandler('tg_bot.log', 'w', 'utf-8')]
)
"""Список використовуваних ботом функцій """
COMMAND_DICT = {}
COMMAND_DICT['command_functions'] = command_functions_list
COMMAND_DICT['message_functions'] = message_functions_list
logging.debug(f'Стартуємо з функціями {COMMAND_DICT}')


class My_tg_bot:
    def __init__(self, token):
        """Створюємо Об'єкт, що слідкує за новинами,
        Вставте токен Вашого бота token_bot.py.default --> token_bot.py >>token = 'Токен Вашого бота'
        """
        self.updater = Updater(token=token)
        """Створюємо Об'єкт, який направляє новину відповідному обробнику"""
        self.dispatcher = self.updater.dispatcher

    """Метод створення обробників згідно списку команд з COMMAND_LIST"""
#TODO розділити меседж хендлери і команд
#TODO меседж хендлери мають бути з фільтрами, щоб при створенні меседжхендлера він 
# створювався з відповідним йому фільтром
#TODO прописати в бот командс сценарій
    def add_command_handlers(self, commands=None):
        for command in commands:
            try:
                self.dispatcher.add_handler(CommandHandler(
                    command, getattr(command_functions, command)))
            except AttributeError:
                logging.error(
                    f'Невідома функція - {command}, додайте її до файлу bot_commands.py')
    def add_message_handlers(self, message_handlers=None, filter=Filters.text & ~Filters.command):
        for function in message_handlers:
            try:
                self.dispatcher.\
                    add_handler(MessageHandler(filter, getattr(message_functions, function)))
            except AttributeError:
                logging.error(
                    f'Невідома функція - {function}, додайте її до файлу bot_commands.py')

    def run(self, command_handlers = None, message_handlers = None):
        """Створюємо обробників"""
        self.add_message_handlers(message_handlers)
        self.add_command_handlers(command_handlers)
        """Слухаємо сервер"""
        self.updater.start_polling()
        self.updater.idle()


if __name__ == '__main__':
    # import toml
    # conf = toml.load(sys.argv[0])
    bot = My_tg_bot(token=token)
    """Запускаємо бота та передаємо йому список команд, які буде використовувати бот"""
    bot.run(command_handlers=command_functions_list, message_handlers=message_functions_list)
