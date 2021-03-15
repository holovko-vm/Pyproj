import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from token_bot import token
import bot_commands

"""Додаємо логування"""
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d.%m.%Y %I:%M',
    level=logging.INFO,
    handlers=[logging.FileHandler('tg_bot.log', 'w', 'utf-8')]
)

"""Список використовуваних ботом функцій """
COMMAND_LIST = ['kill', 'commands', 'echo','givno']
logging.debug(f'Стартуємо з функціями {COMMAND_LIST}')

class My_tg_bot:
    def __init__(self, token):
        """Створюємо Об'єкт, що слідкує за новинами,
        Вставте токен Вашого бота token_bot.py.default --> token_bot.py >>token = 'Токен Вашого бота'
        """
        self.updater = Updater(token=token)
        """Створюємо Об'єкт, який направляє новину відповідному обробнику"""
        self.dispatcher = self.updater.dispatcher

    """Метод створення обробників згідно списку команд з COMMAND_LIST"""
    def add_handlers(self, command):
        try:
            if command == 'echo':
                self.dispatcher.\
                    add_handler(MessageHandler(Filters.text & ~Filters.command, getattr(bot_commands, 'echo')))
                return
            self.dispatcher.add_handler(CommandHandler(command, getattr(bot_commands, command)))
        except AttributeError:
            logging.error(f'Невідома функція - {command}, додайте її до файлу bot_commands.py')

    def run(self, args):
        """Створюємо обробників"""
        for _ in args:
            self.add_handlers(_)
        """Слухаємо сервер"""
        self.updater.start_polling()
        self.updater.idle()

if __name__ == '__main__':
    bot = My_tg_bot(token=token)
    """Запускаємо бота та передаємо йому список команд, які буде використовувати бот"""
    bot.run(COMMAND_LIST)