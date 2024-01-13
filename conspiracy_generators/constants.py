import json

# Bot Command Constants
HELP_MESSAGE = """
Greetings, 'human'. What do you seek?

(I've been abducted please send help)

/help - Send this help message
/truth - Generates a random truth
/listall - Lists all keywords
"""
ADD_DELETE = """
add <command> <response> - adds or edits a command
delete <command> - deletes a command
"""


COMMANDS = json.loads(open("conspiracy_generators/commands.json", "r").read())
COMMANDS.update(json.loads(open("conspiracy_generators/people.json", "r").read()))


def listall():
    all_commands = f"Command Options:\n"
    commands = json.loads(open("conspiracy_generators/commands.json", "r").read())
    for key in commands.keys():
        all_commands = all_commands + f"/{key}\n"
    return all_commands


BOT_FUNCTIONS = {
    "start": "The government is run by aliens!",
    "help": HELP_MESSAGE,
    "listall": listall(),
    "command_not_found": "Error, commmand not recognized: ",
}

# Neural Blender Constants
IMG_PATH = "conspiracy_bot/generators/images/"
ERROR_IMG = IMG_PATH + "error_img.png"


GROUPME_BASEURL = "https://api.groupme.com/v3"
