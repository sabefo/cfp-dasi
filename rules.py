# coding=utf-8
from pyknow import *


class ChatBotRules(KnowledgeEngine):
    bot = None

    def setBot(self, bot):
        self.bot = bot

    @Rule(Fact(intent='Balance'))
    def ruleGiveBalance(self):
        # quiero el balance
        self.bot.responseAccountBalance()

    @Rule(Fact(intent='Movimiento - Ingreso'))
    def ruleNotUnderstood(self):
        # no te entiendo
        self.bot.responseIncome()

    @Rule(Fact(intent='Compra'))
    def ruleUserBuys(self):
        # quiero el balance
        self.bot.responseBuy()
