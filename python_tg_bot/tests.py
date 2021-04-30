import unittest
from unittest import TestCase
from unittest.mock import patch, Mock
from tg_bot import My_tg_bot
from command_functions import command_functions_list


class Test(TestCase):
    def test_run_add_all_handlers(self):
        """Перевіряє додавання всіх обробників, включно з обробником повідомлень та запуск бота"""
        with patch('tg_bot.Updater'):
            bot = My_tg_bot('')
            bot.dispatcher.add_handler = Mock()
            bot.run(command_handlers=command_functions_list)
            assert bot.dispatcher.add_handler.call_count - 1 == len(command_functions_list)

if __name__ == '__main__':
    unittest.main()