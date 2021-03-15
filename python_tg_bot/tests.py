import unittest
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from unittest import TestCase
from unittest.mock import patch, Mock
from unittest import mock
import python_tg_bot
from python_tg_bot import tg_bot, bot_commands
from tg_bot import My_tg_bot


class Test(TestCase):
    def test_run(self):
        with patch('tg_bot.Updater'):
            bot = My_tg_bot('')
            bot.add_handlers = Mock()
            bot.run(args=[])



if __name__ == '__main__':
    unittest.main()