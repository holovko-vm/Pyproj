import  unittest
from unittest import  TestCase
from  unittest.mock import patch
import python_tg_bot
from python_tg_bot import tg_bot, bot_commands

class Test(TestCase):
    def test1(self):
        with patch('tg_bot.Updater'):
            bot = tg_bot.My_tg_bot('')
            print('some')