import unittest
from unittest import TestCase
from unittest.mock import patch, Mock
from tg_bot import My_tg_bot



class Test(TestCase):
    def test_run(self):
        with patch('tg_bot.Updater'):
            bot = My_tg_bot('')
            bot.add_handlers = Mock()
            call_count = 5
            call_count_list = []
            '''Перевіряємо, чи дійсно run викликає функцію створення Хендлерів'''
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
                '''Якщо тут нема помилки, то значить Хендлер додано'''
                result_call += 1
            self.assertEqual(call_count, result_call)

    def test_handlers2(self):
        COMMAND_LIST = ['kill', 'commands', 'echo']
        '''Тут несправжній токен'''
        bot = My_tg_bot(token='1644418380:AAGfEIP4Z4rZEZieQjueQNWf_C0r7FW0h_A')
        call_count = 1
        '''Створюємо Хендлери'''
        for _ in COMMAND_LIST:
            call_count += 1
            bot.add_handlers(command=f'{_}')
        '''Визначаємо кількість створених Хендлерів'''
        result = 1
        for _ in bot.updater.dispatcher.handlers[0]:
            result += 1
        '''Перевіряємо кількості вискликаних і створених Хендлерів'''
        self.assertEqual(result, call_count)

if __name__ == '__main__':
    unittest.main()