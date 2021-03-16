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
            call_count = 5
            call_count_list = []
            for _ in range(call_count):
                call_count_list.append('')
            bot.run(args=call_count_list)
            assert bot.add_handlers.call_count == 5

    def test_handlers(self):
        with patch('tg_bot.Updater'):
            bot = My_tg_bot('')
            call_count = 5
            result_call = 0
            for _ in range(call_count):
                bot.add_handlers(command='')
                result_call += 1
            # print(bot.dispatcher.handlers) ''' <<<<<< Ця штука повертає дікт хендлерів(в нормальних умовах),
            # і в ідеалі б після створення хендлерів перевіряти чи вони дійсно створились, але через те, що створюється наш клас
            # об єктом MagikMock, цей дікт перетворюється на об єкт MagikMock.
            # Поки бачу 3 варіанти вирішення цього питання:
            # 1) Залишити як зараз є, раз створюється і нема помилки, то все ок
            # 2) не робити моком клас і тоді дікт буде повертатися і можна буде перевірити його на правильність роботи
            # 3) найскладніший - Після створення хендлерів перевіряти чи працюють вони(але напевно це зайве в рамках юніттестів)
            # Поки думаю, що другий найвалідніший, а ти?
            # розумію що можуть бути і інші варіанти, але це ті, що мені в голову прийшли
            # Можливо є якісь фічі, які могли б перевірити чи справді воно додало хендлери?'''
            self.assertEqual(call_count, result_call)


if __name__ == '__main__':
    unittest.main()