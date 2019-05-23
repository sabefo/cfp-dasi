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

    @Rule(Fact(intent = 'Movimiento - ingreso'),
          OR(Fact(intent='Movimiento - gasto')))
    def ruleInsertMovement(self):
        # quiero guardar un movimiento
        self.bot.responseInsertMovement()

    @Rule(Fact(intent='Compra'))
    def ruleUserBuys(self):
        # quiero comprar algo
        self.bot.responseBuy()