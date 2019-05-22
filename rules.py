# coding=utf-8
from pyknow import *


class ChatBotRules(KnowledgeEngine):
    bot = None

    def setBot(self, bot):
        self.bot = bot

    @Rule(Fact(intent='Balance'))
    def ruleGiveBalance(self):
        # quiero el balance
        self.bot.responseBalance()

    @Rule(Fact(intent='Movimiento - Ingreso'))
    def ruleNotUnderstood(self):
        # no te entiendo
        self.bot.responseIncome()

# from pyknow import *

# class Greetings(KnowledgeEngine):
#     @DefFacts()
#     def _initial_action(self):
#         yield Fact(action="greet")

#     @Rule(Fact(action='greet'),
#         NOT(Fact(name=W())))
#     def ask_name(self):
#         self.declare(Fact(name=input("What's your name? ")))

#     @Rule(Fact(action='greet'),
#         NOT(Fact(location=W())))
#     def ask_location(self):
#         self.declare(Fact(location=input("Where are you? ")))

#     @Rule(Fact(action='greet'),
#         Fact(name=MATCH.name),
#         Fact(location=MATCH.location))
#     def greet(self, name, location):
#         print("Hi %s! How is the weather in %s?" % (name, location))

# engine = Greetings()
# engine.reset() # Prepare the engine for the execution.
# engine.run() # Run it!