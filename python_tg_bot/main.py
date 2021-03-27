import logging
"""Додаємо логування"""
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d.%m.%Y %I:%M',
    level=logging.DEBUG,
    handlers=[logging.FileHandler('tg_bot.log', 'w', 'utf-8')]
)

if __name__ == '__main__':
    from token_bot import token
    from tg_bot import My_tg_bot
    from command_functions import command_functions_list
    from message_functions import message_functions_dict
    logging.info("start")

    bot = My_tg_bot(token=token)
    """Запускаємо бота та передаємо йому список команд, які буде використовувати бот"""
    bot.run(command_handlers=command_functions_list,
            message_handlers=message_functions_dict)
