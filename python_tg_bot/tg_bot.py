import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
token = "1602418380:AAGfEIP4Z4rZEZieQjueQNWf_C0r7FW0h_A"
logger = logging.getLogger(__name__)
class My_tg_bot:
    def __init__(self, token):
        self.updater = Updater(token=token)
        self.dispatcher = self.updater.dispatcher

    def commands(self, update: Update, context: CallbackContext) -> None:
        """Send a message when the command /start is issued."""
        update.message.reply_text(f'принято команду - {update.message.text}')

    def echo(self, update: Update, context: CallbackContext) -> None:
        """Echo the user message."""
        update.message.reply_text(update.message.text)

    def add_handlers(self, command):
        self.dispatcher.add_handler(CommandHandler(f'{command}', self.commands))
        self.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, self.echo))



    def run(self):
        self.add_handlers(command='start')
        self.updater.start_polling()
        self.updater.idle()

if __name__ == '__main__':
    bot = My_tg_bot(token=token)
    bot.run()