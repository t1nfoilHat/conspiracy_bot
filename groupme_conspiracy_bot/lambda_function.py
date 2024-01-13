import logging
import json
from groupme_bot import GroupmeBot
import yaml
from yaml import Loader

LOG = logging.getLogger()
LOG.setLevel(logging.INFO)


def lambda_handler(event, context):

    LOG.info(event.get("body"))

    with open("groupme_bot_config.yml", "r") as config:
        config = yaml.load(config, Loader=Loader)

    BOT_NAME = config.get("groupme").get("bot_name")
    BOT_ID = config.get("groupme").get("bot_id")
    GROUP_ID = config.get("groupme").get("group_id")
    ACCESS_TOKEN = config.get("groupme").get("access_token")

    groupmeBot = GroupmeBot(BOT_NAME, BOT_ID, GROUP_ID, ACCESS_TOKEN)
    groupmeBot.handle_event(event)
