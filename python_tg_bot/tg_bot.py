import logging
from telegram.ext import Updater
from bot_commands import COMMAND_LIST, COMMAND_DICT
import exeptions
import sys

"""Додаємо логування"""
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d.%m.%Y %I:%M',
    level=logging.INFO,
    handlers=[logging.FileHandler('tg_bot.log', 'w', 'utf-8')]
)

logging.debug(f'Стартуємо з функціями {COMMAND_LIST}')


class My_tg_bot:
    def __init__(self, token, commands_dict=COMMAND_DICT):
        """Створюємо Об'єкт, що слідкує за новинами,
        Вставте токен Вашого бота token_bot.py.default --> token_bot.py >>token = 'Токен Вашого бота'
        """
        self.updater = Updater(token=token)
        """Створюємо Об'єкт, який направляє новину відповідному обробнику"""
        self.dispatcher = self.updater.dispatcher
        self.commands_dict = commands_dict

    def add_handlers(self, command):
        """Метод створення обробників згідно списку команд з COMMAND_LIST"""
        cmd = self.commands_dict.get(command, None)
        if cmd is None:
            raise exeptions.CommandNotExist(command)
        self.dispatcher.add_handler(cmd)

    def run(self, command_names):
        """Створюємо обробників"""
        for name in command_names:
            self.add_handlers(name)

        """Слухаємо сервер"""
        self.updater.start_polling()
        self.updater.idle()


if __name__ == '__main__':
    from token_bot import token
    # import toml
    # conf = toml.load(sys.argv[0])
    bot = My_tg_bot(token=token)
    """Запускаємо бота та передаємо йому список команд, які буде використовувати бот"""
    try:
        bot.run(COMMAND_LIST)
    except exeptions.CommandNotExist as err:
        logging.error(
            f'error: {err}')
