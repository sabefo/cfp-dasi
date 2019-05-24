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

    @Rule(Fact(intent='Ingreso'))
    def ruleInsertIncome(self):
        # quiero el balance
        self.bot.responseInsertIncome()

    @Rule(Fact(intent='Egreso'))
    def ruleInsertExpense(self):
        # quiero el balance
        self.bot.responseInsertExpense()

    @Rule(Fact(intent='Compra'))
    def ruleUserBuys(self):
        # quiero comprar algo
        self.bot.responseBuy()

    @Rule(Fact(intent='Si'))
    def ruleUserAgrees(self):
        # quiero comprar algo
        self.bot.responseAgrees()

    @Rule(Fact(intent='No'))
    def ruleUserDisagrees(self):
        # quiero comprar algo
        self.bot.responseDisagrees()
