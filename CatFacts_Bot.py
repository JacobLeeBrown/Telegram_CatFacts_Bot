from random import randrange

class CatFacts_Bot(object):

    def __init__(self, facts):
        self.facts = facts
        self.size = len(facts)
        self.randrange = randrange

    def fact_me(self, bot, update):
        text = self.facts[self.randrange(self.size)]
        bot.send_message(chat_id=update.message.chat_id, text=text)
