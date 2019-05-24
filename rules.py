# coding=utf-8
# https://github.com/buguroo/pyknow
from pyknow import *

# Clase donde se contemplan todas reglas del sistema.
class ChatBotRules(KnowledgeEngine):
    bot = None

    # Método que recibe el bot y lo inicializa para las reglas
    def setBot(self, bot):
        self.bot = bot

    # Regla que saluda al usuario personalizado con su nombre
    @Rule(Fact(intent='Saludo'))
    def ruleGreet(self):
        name = self.bot.message['from']['first_name']
        self.bot.responseGreet(name)

    # Regla para mostrar el balance de cuenta del usuario
    @Rule(Fact(intent='Balance'))
    def ruleGiveBalance(self):
        self.bot.responseAccountBalance()

    # Regla para meter un ingreso a la base de datos
    @Rule(Fact(intent='Ingreso'))
    def ruleInsertIncome(self):
        self.bot.responseInsertIncome()

    # Regla para meter un egreso a la base de datos
    @Rule(Fact(intent='Egreso'))
    def ruleInsertExpense(self):
        self.bot.responseInsertExpense()

    # Regla para decirle al sistema que el usuario quiere comprar un producto y mostrarle opciones específicas
    @Rule(Fact(intent='Compra'))
    def ruleUserBuys(self):
        self.bot.responseBuy()

    # Regla para agregar el producto comprado a la base de datos junto y también contemplarlo como un egreso
    @Rule(Fact(intent='Si'))
    def ruleUserAgrees(self):
        self.bot.responseAgrees()

    # Regla para pedirle al sistema que muestre un producto nuevo
    @Rule(Fact(intent='No'))
    def ruleUserDisagrees(self):
        self.bot.responseDisagrees()