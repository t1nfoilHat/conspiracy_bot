# STL
from time import sleep
import random
import logging
import json
import re

# PDM
import requests
from requests.models import Response

# LOCAL
from conspiracy_generators.constants import (
    COMMANDS,
    BOT_FUNCTIONS,
    ERROR_IMG,
    IMG_PATH,
)
from conspiracy_generators.constants import GROUPME_BASEURL as BASE_URL
from conspiracy_generators.random_conspiracy_generator import get_conspiracy

COMMAND_PATTERN = r".*?(/\w+)|((/\w+)\W\.*?)"

LOG = logging.getLogger()
LOG.setLevel(logging.INFO)


class GroupmeBot:
    def __init__(self, bot_name: str, bot_id: str, group_id: str, access_token: str):
        self.bot_name = bot_name
        self.bot_id = bot_id
        self.group_id = group_id
        self.access_token = access_token
        self.recent_message_id = None

    def post_response(self, resp_str: str):
        data = json.dumps(
            {
                "bot_id": self.bot_id,
                "text": resp_str,
            }
        )
        url = BASE_URL + "/bots/post"
        r = requests.post(url, data=data)
        print(r.text)

    def handle_command(self, command: str):
        val = COMMANDS.get(command)
        if not val:
            val = BOT_FUNCTIONS.get(command)
        if val:
            self.post_response(val)
        elif command == "truth":
            self.post_response(get_conspiracy())
        else:
            self.post_response(BOT_FUNCTIONS.get("command_not_found") + command)

    def parse_message_text(self, message: str):
        if "/" in message:
            # FIX THIS SOMEDAY
            command = re.compile(COMMAND_PATTERN)
            command_str = command.match(message)[0]
            self.handle_command(command_str[1:])

    def handle_event(self, event: dict):
        body_dict = json.loads(event.get("body"))
        sender_name = body_dict.get("name")
        sender_group_id = body_dict.get("group_id")
        message = body_dict.get("text")

        if (sender_name != self.bot_name) and (sender_group_id == self.group_id):
            LOG.info(
                f"Responding to message: {message}\nsender_name: {sender_name}\nbot_name: {self.bot_name}\nsender_group_id: {sender_group_id}\nbot_group_id: {self.group_id}"
            )
            self.parse_message_text(message)
        else:
            LOG.info(
                f"NOT Responding to message: {message}\nsender_name: {sender_name}\nbot_name: {self.bot_name}\nsender_group_id: {sender_group_id}\nbot_group_id: {self.group_id}"
            )
