# STL
import random
import logging

# PDM
from telegram import Update
from telegram.bot import Bot
from telegram.ext import Updater, CommandHandler, CallbackContext

# LOCAL
from conspiracy_generators.random_conspiracy_generator import get_conspiracy
from conspiracy_generators.constants import (
    COMMANDS,
    BOT_FUNCTIONS,
    ERROR_IMG,
    IMG_PATH,
)

LOG = logging.getLogger()


def _5GHorse(update: Update, context: CallbackContext):
    context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open(IMG_PATH + "5GHorse.png", "rb"),
    )


class TelegramBot:
    def __init__(self, token):
        self.token = token

    def bot_function(self, update: Update, context: CallbackContext):
        key = update.message.text[1:]
        val = BOT_FUNCTIONS.get(key)
        update.message.reply_text(val)

    def command(self, update: Update, context: CallbackContext):
        key = update.message.text.split()[0][1:]  # parse out command to use as dict key
        prompt = COMMANDS.get(key)
        if key == "5G":
            _5GHorse(update, context)
        else:
            update.message.reply_text(prompt)

    def truth(self, update: Update, context: CallbackContext):
        prompt = get_conspiracy()
        update.message.reply_text(prompt)

    def start(self):
        # Initialize bot updater
        updater = Updater(token=self.token, use_context=True)
        dispatcher = updater.dispatcher

        # Define command functions
        dispatcher.add_handler(
            CommandHandler([key for key in BOT_FUNCTIONS.keys()], self.bot_function)
        )
        dispatcher.add_handler(
            CommandHandler(
                [key for key in COMMANDS.keys()], self.command, pass_args=True
            )
        )
        dispatcher.add_handler(CommandHandler("truth", self.truth, pass_args=True))

        # Start bot
        updater.start_polling()
