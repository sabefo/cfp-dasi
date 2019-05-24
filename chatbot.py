# coding=utf-8
import json
import mercado_libre
import database
import pprint
import rules
import telepot
from telepot.loop import MessageLoop
import time
import urllib
import dialogflow_v2 as dialogflowAPI
import dialogflow
import os
from pyknow import *
import rules

#Credenciales para la conexión entre Python y DialogFlow
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "halogen-oxide-225816-facf749e60d7.json"
DIALOGFLOW_PROJECT_ID = 'halogen-oxide-225816'
GOOGLE_APPLICATION_CREDENTIALS = 'halogen-oxide-225816-facf749e60d7.json'
SESSION_ID = 'proyectodasiucm'

#Clase principal del chatbot donde se realiza todo el manejo del mismo.
class Chatbot():
    # Variables auxiliares necesarias para hacer funcionar la clase
    meli = None
    response = None
    userConversation = None
    chatBotRules = None
    chat_id = None
    total = None
    current_item = 0
    searchText = None
    params = None
    price = 0
    title = None

    #Se instancia DialogFlow, el bot de Telegram y el manejador de reglas.
    def __init__(self):
        # Credencial de Telegram para interactuar con el usuario
        TOKEN = '894407782:AAHlyE4ko1wbWlj_oU-utzzBI0weSkC-4Pk'
        session_client = dialogflowAPI.SessionsClient()
        session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
        self.userConversation = dialogflow.testingDialogflow()
        self.bot = telepot.Bot(TOKEN)
        self.chatBotRules = rules.ChatBotRules()
        self.chatBotRules.setBot(self)
        MessageLoop(self.bot, self.manageMessage).run_as_thread()
        print('Listening ...')

        while 1:
            time.sleep(10)

    # Método que interactúa con Telegram
    def manageMessage(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        self.chat_id = chat_id

        user = [[chat_id, msg['from']['first_name'],msg['from']['last_name']]]
        database.insertUser(user)

        # mensaje del usuario
        self.message = msg
        self.intents = self.userConversation.get_all_intents()

        self.response = self.userConversation.detect_intent_texts(DIALOGFLOW_PROJECT_ID,SESSION_ID,self.message['text'],'es')
        self.chatBotRules.reset()

        if self.response['intent'] != '':
            self.chatBotRules.declare(Fact(intent = self.response['intent']))
        print(self.chatBotRules.facts)

        # ejecutamos el motor de reglas
        if self.response['allParamsPresent'] != False:
            self.chatBotRules.run()

        self.bot.sendMessage(self.chat_id, self.response["responseText"])

    # Método que contacta a mercado libre con la búsqueda que desea realizar el usuario
    # y regresa el producto que se va a mostrar, en caso de no querer dicho producto muestra otro.
    # Recibe el mensaje del usuario y también el número ítem que se está buscando, siempre inicia en 0
    def contactMercadoLibre(self, chat_id, msg, current_item):
        self.meli = mercado_libre.MercadoLibre()
        self.chat_id = chat_id
        meli_answer = self.meli.formatJSON(self.meli.searchProduct(msg))
        self.total = len(meli_answer)
        self.params = self.response["paramsData"]
        if self.total == 0:
            "No hay ese tipo de producto"
        elif current_item <= self.total and meli_answer[current_item]:
            message = meli_answer[current_item]["link"] + "\n"
            if meli_answer[current_item]["reviews"]:
                message += "Su calificación según los usuarios es " + str(meli_answer[current_item]["reviews"]["rating_average"]) + "/5"
                message += " de un total de " + str(meli_answer[current_item]["reviews"]["total"]) + " evaluaciones" + " \n"
            message += "Su precio es de: $" + str(meli_answer[current_item]["price"])
            self.title = meli_answer[current_item]["title"]
            self.price = meli_answer[current_item]["price"]
            self.bot.sendMessage(chat_id, message)
            self.bot.sendPhoto(chat_id, meli_answer[current_item]["photo"]);

    # Respuesta del sistema cuando se cae en la regla de ruleInsertIncome
    # Mete a la base de datos un ingreso
    def responseInsertIncome(self):
        tipo = self.response["paramsData"]["Ingreso"]
        amount = self.response["paramsData"]["unit-currency"]["amount"]
        concept = self.response["paramsData"]["Concepto"]
        database.insertTransaction(self.chat_id, tipo, amount, concept)

    # Respuesta del sistema cuando se cae en la regla de ruleInsertExpense
    # Mete a la base de datos un egreso
    def responseInsertExpense(self):
        tipo = self.response["paramsData"]["Egreso"]
        amount = self.response["paramsData"]["unit-currency"]["amount"]
        concept = self.response["paramsData"]["Concepto"]
        database.insertTransaction(self.chat_id, tipo, amount, concept)

    # Respuesta del sistema cuando se cae en la regla de ruleGiveBalance
    # Regresa el balance del usuario, en caso de no tener información regresa un mensaje correspondiente
    def responseAccountBalance(self):
        print(self.chat_id)
        balance = database.getOverallBalance(self.chat_id)
        if balance["overall"] == None:
            self.bot.sendMessage(self.chat_id, "Oops, no dispones de ingresos o egresos registrados en el sistema. 🗄" )
        else:
            self.bot.sendMessage(self.chat_id, "Su balance general es de: $%8.2f \nSu mayor ingreso viene de: Sueldo. 💰 \nSu mayor gasto es en: Renta. 🏘 \nEn total: %s ingresos y %s egresos. " %(balance["overall"], balance["ingresos"], balance["egresos"]) )

    # Respuesta del sistema cuando se cae en la regla de ruleUserBuys
    # Muestra los productos que aparecen en Mercado Libre
    def responseBuy(self):
        if self.response["allParamsPresent"]:
            self.searchText = self.response["searchText"]
            self.current_item = 0
            self.contactMercadoLibre(self.chat_id, self.searchText, self.current_item)

    # Respuesta del sistema cuando se cae en la regla de ruleUserAgrees
    # Mete en la base de datos el producto comprado y también registra la cantidad como egreso
    def responseAgrees(self):
        tipo = "Egreso"
        amount = self.price
        concept = self.title
        database.insertTransaction(self.chat_id, tipo, amount, concept)
        database.insertProduct(self.chat_id, concept, amount)
        self.bot.sendMessage(self.chat_id, 'Perfecto, compra registrada.')

    # Respuesta del sistema cuando se cae en la regla de ruleUserAgrees
    # regresa al método de contactMercadoLibre pero esta vez aumenta en uno el número del ítem a mostrar
    def responseDisagrees(self):
        self.current_item += 1
        self.contactMercadoLibre(self.chat_id, self.searchText, self.current_item)

    # Respuesta del sistema cuando se cae en la regla de ruleGreet
    # Recibe el nombre del usuario y lo saluda
    def responseGreet(self, nombre):
        self.bot.sendMessage(self.chat_id, '📣 Hola ' + nombre +  '! 😀' )


if __name__ == '__main__':
    chatbot = Chatbot()
