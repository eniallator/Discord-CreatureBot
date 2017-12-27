"""Commands for the CreatureBot"""
from src.CommandSystem import CommandSystem

COMMANDS = CommandSystem()


async def _add(client, user_cmd, message):
    pass

COMMANDS.add_command(
    'add',
    cmd_func=_add,
    cmd_help=lambda client, user_cmd, message: 'Add a creature to the list'
)


async def _remove(client, user_cmd, message):
    pass

COMMANDS.add_command(
    'remove',
    cmd_func=_remove,
    cmd_help=lambda client, user_cmd, message: 'Remove a creature to the list'
)


async def _list(client, user_cmd, message):
    pass

COMMANDS.add_command(
    'list',
    cmd_func=_list,
    cmd_help=lambda client, user_cmd, message: 'Lists all the creatures currently'
)
