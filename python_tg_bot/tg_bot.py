import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from token_bot import token
import bot_commands
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)
# TODO написати коректне логування і тести
# def echo(update: Update, context: CallbackContext) -> None:
#     """Ехо-відповідь користувачу"""
#     update.message.reply_text(update.message.text)
#
# def commands(update: Update, context: CallbackContext) -> None:
#     """Список використовуваних ботом команд"""
#     update.message.reply_text(f'Список доступних команд - {COMMAND_LIST}')
#
# def kill(update: Update, context: CallbackContext) -> None:
#     """Фан-функція, формат виклику /kill 'name' """
#     update.message.reply_text(f'We will kill {update.message.text[6:]} for you')


"""Список використовуваних ботом функцій """
COMMAND_LIST = ['kill', 'commands', 'echo']

class My_tg_bot:
    def __init__(self, token):
        """Створюємо Об'єкт, що слідкує за новинами"""
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
        except NameError as namerr:
            print(f'Невідома функція - {namerr}')

    def run(self, args):
        """Створюємо обробників"""
        for _ in args:
            self.add_handlers(_)
        """Слухаємо сервер"""
        self.updater.start_polling()
        self.updater.idle()

if __name__ == '__main__':
    bot = My_tg_bot(token=token)
    bot.run(COMMAND_LIST)