from .bot_commands import *

__ALL__ = ["COMMAND_LIST", "COMMAND_DICT"]

"""Список використовуваних ботом функцій """
COMMAND_LIST = ['echo', 'commands', 'kill', 'givno']
COMMAND_DICT = {
    "echo": MessageHandler(Filters.text & ~Filters.command, echo),
    "commands": CommandHandler("commands", commands),
    "kill": CommandHandler("kill", kill),
}
