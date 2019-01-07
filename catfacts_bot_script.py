
import my_env as env

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, BaseFilter

import logging as lg

from CatFacts_Bot import CatFacts_Bot

# Basic logging
lg.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
               level=lg.INFO)
logger = lg.getLogger(__name__)

def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)

# # User Whitelist Filter # Not needed for this bot, everyone can enjoy!
# class WhitelistFilter(BaseFilter):
#     def __init__(self, whitelist):
#         self.whitelist = whitelist

#     def filter(self, message):
#         return message.from_user.id in self.whitelist


def main():
    # Initialize bot (telegram)
    updater = Updater(token=env.catfacts_token)
    dp = updater.dispatcher
    # Initialize CatFacts wrapper (requires facts list)
    facts = []
    f = open('catfacts.txt', 'r')
    for line in f:
        facts.append(line[:-1])
    my_bot = CatFacts_Bot(facts)
    # Initialize whitelist filter
    #my_filter = WhitelistFilter(env.user_whitelist)

    # Register commands with the Telegram Bot
    fact_me_handler = CommandHandler('fact_me', my_bot.fact_me)
    dp.add_handler(fact_me_handler)

    # Log errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()

# Run from Python CLI with (Python 3):
# >>> exec(open("catfacts_bot_script.py").read())