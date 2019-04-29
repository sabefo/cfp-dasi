from pyknow import *

class EatBotRules(KnowledgeEngine):
    bot = None

    def setBot(self, bot):
        self.bot = bot


    @Rule(Fact(intent='Default Fallback Intent'))
    def ruleNotUnderstood(self):
        # no te entiendo
        self.bot.responseNotUnderstood()

    @Rule(Fact(intent='greet'))
    def ruleGreet(self):
        # saludar al usuario
        name = self.bot.message['from']['first_name']
        self.bot.responseGreet(name)
