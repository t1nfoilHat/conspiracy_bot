# Conspiracy Bot

Fun little bot that sends random conspiracies to Telegram and Groupme

All code is final, and probably does not work. No warranty included.

## Getting Started

1. For Telegram create `telegram_bot/telegram_bot_config.yml` to include the credentials for your bot(s)
   Format:
   ```
   conspiracy1947_bot:
      name: "conspiracy1947_bot"
      token: "<your token>"
   conspiracy2012_bot:
      name: "conspiracy2012_bot"
      token: "<your token>"
   ```
2. For Groupme create `groupme_conspiracy_bot/groupme_bot_config.yml` to include the credentials for your bot
   ```
   groupme:
      bot_name: "conspiracy_bot"
      bot_id: "<your bot id>"
      group_id: "<group id to add>"
      access_token: "<your access token>"
   ```
   The groupme bot also has some commands to deploy it as an AWS Lambda function. Unfortunately, I no longer remember how to do this. Good luck have fun!
3. `pdm run python main.py [arg]`
   args: --telegram, --groupme(TODO)

## Adding prompts

All hardcoded prompts can be added or edited in `generators.constants.py`
