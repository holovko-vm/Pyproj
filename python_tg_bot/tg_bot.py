import logging
from token import token
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

def echo(update: Update, context: CallbackContext) -> None:
    """Ехо-відповідь користувачу"""
    update.message.reply_text(update.message.text)

def commands(update: Update, context: CallbackContext) -> None:
    """Список використовуваних ботом команд"""
    update.message.reply_text(f'Список доступних команд - {COMMAND_LIST}')

def kill(update: Update, context: CallbackContext) -> None:
    """Фан-функція, формат виклику /kill 'name' """
    update.message.reply_text(f'We will kill {update.message.text[6:]} for you')

COMMAND_LIST = ['kill', 'commands', 'echo']
logger = logging.getLogger(__name__)

class My_tg_bot:
    def __init__(self, token):
        self.updater = Updater(token=token)
        self.dispatcher = self.updater.dispatcher

    def add_handlers(self, args):
        try:
            if args == 'echo':
                self.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
                return
            _ = eval(args)
            self.dispatcher.add_handler(CommandHandler(args, _))
        except NameError as namerr:
            print(f'Отсутствует такая функция {namerr}')


    def run(self, args):
        for _ in args:
            self.add_handlers(_)
        self.updater.start_polling()
        self.updater.idle()




if __name__ == '__main__':
    bot = My_tg_bot(token=token)
    bot.run(COMMAND_LIST)