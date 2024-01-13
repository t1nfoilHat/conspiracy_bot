import yaml
from yaml import Loader
import argparse
from telegram_bot import TelegramBot


def main(argv):

    with open("telegram_bot/telegram_bot_config.yml", "r") as config:
        config = yaml.load(config, Loader=Loader)

    if argv.bot_1947:
        token = config.get("conspiracy1947_bot").get("token")
        telegramBot1947 = TelegramBot(token)
        telegramBot1947.start()
    if argv.bot_2012:
        token = config.get("conspiracy2012_bot").get("token")
        telegramBot2012 = TelegramBot(token)
        telegramBot2012.start()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Start telegram bot that generate random conspiracies"
    )
    parser.add_argument("--1947", dest="bot_1947", default=False, action="store_true")
    parser.add_argument("--2012", dest="bot_2012", default=False, action="store_true")

    ARGV = parser.parse_args()

    main(ARGV)
