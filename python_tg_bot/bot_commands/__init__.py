from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackContext
import bot_commands.bot_command_handlers as c_handlers
import bot_commands.bot_message_handlers as m_handlers
from bot_commands.bot_command_handlers import COMMAND_LIST
__all__ = ["COMMAND_LIST", "COMMAND_DICT"]

"""Список використовуваних ботом функцій """
messages_handlers = ['echo']
command_handlers = ['commands', 'kill']


COMMAND_DICT = {
    "echo": MessageHandler(Filters.text & ~Filters.command, m_handlers.echo),
}

COMMAND_LIST.extend(messages_handlers)
COMMAND_LIST.extend(command_handlers)

for ch in command_handlers:
    COMMAND_DICT[ch] = CommandHandler(ch, getattr(c_handlers, ch))
