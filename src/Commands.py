"""Commands for the CreatureBot"""
from src.CommandSystem import CommandSystem

COMMANDS = CommandSystem()


async def _add(client, user_cmd, message):
    pass

COMMANDS.add_command(
    'add',
    cmd_func=_add,
    cmd_help=lambda client, user_cmd, message: 'Add creature(s) to the list',
    specific_help=lambda client, user_cmd, message: 'Add creature(s) like so: `add giraffe lion:2 argy:4`'
)


async def _remove(client, user_cmd, message):
    pass

COMMANDS.add_command(
    'remove',
    cmd_func=_remove,
    cmd_help=lambda client, user_cmd, message: 'Remove creature(s) from the list',
    specific_help=lambda client, user_cmd, message: 'Remove creature(s) like so: `remove giraffe lion:2 argy:4`'
)


async def _clear(client, user_cmd, message):
    pass

COMMANDS.add_command(
    'clear',
    cmd_func=_clear,
    cmd_help=lambda client, user_cmd, message: 'Clear creature(s) from the list',
    specific_help=lambda client, user_cmd, message: 'Clear creature(s) like so: `clear giraffe lion argy`'
)


async def _list(client, user_cmd, message):
    pass

COMMANDS.add_command(
    'list',
    cmd_func=_list,
    cmd_help=lambda client, user_cmd, message: 'Lists all the creatures currently'
)
