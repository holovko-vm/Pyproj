import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)


def commands(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text(f'принято команду - {update.message.text}')
def kill(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'We kill you')
commandsr = ['rakuvaln9', 'rak', 'givno', 'kill', 'commands']
token = "1602418380:AAGfEIP4Z4rZEZieQjueQNWf_C0r7FW0h_A"
logger = logging.getLogger(__name__)
class My_tg_bot:
    def __init__(self, token):
        self.updater = Updater(token=token)
        self.dispatcher = self.updater.dispatcher

    def echo(self, update: Update, context: CallbackContext) -> None:
        """Echo the user message."""
        update.message.reply_text(update.message.text)


    def add_command_handlers(self, *args):
        for _ in args:
            if _ == 'kill':
                self.dispatcher.add_handler(CommandHandler(f'{_}', kill))
            self.dispatcher.add_handler(CommandHandler(f'{_}', commands))


    def add_handlers(self):
        self.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, self.echo))

    def run(self, args):
        for _ in args:
            self.add_command_handlers(_)
        self.add_handlers()
        self.updater.start_polling()
        self.updater.idle()




if __name__ == '__main__':
    bot = My_tg_bot(token=token)
    bot.run(commandsr)