import  unittest
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from unittest import  TestCase
from unittest.mock import patch
from unittest import mock
import python_tg_bot
from python_tg_bot import tg_bot, bot_commands


# class Test(TestCase):
#     def test1(self):
#         with patch('tg_bot.Updater'):
#             bot = tg_bot.My_tg_bot('')
#             bot.run()

def givno(args):
    for _ in range(len(args)):
        args[_]+=1
    return args

class Test(TestCase):
    def test_ok(self):
        kil = givno([1,2,3,4])
        self.assertEqual(kil,[2,3,4,5])


if __name__ == '__main__':
    unittest.main()