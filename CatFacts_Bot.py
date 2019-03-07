from random import randrange

class CatFacts_Bot(object):

    def __init__(self, facts):
        self.facts = facts
        self.size = len(facts)
        self.randrange = randrange

    def fact_me(self, update, context):
        text = self.facts[self.randrange(self.size)]
        context.bot.send_message(chat_id=update.message.chat_id, text=text)
