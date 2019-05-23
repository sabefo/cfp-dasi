# coding=utf-8
import dialogflow
import dialogflow_v2 as dialogflowAPI
import json
import mercado_libre
import os
import pprint
from pyknow import *
import requests
import rules
import telepot
from telepot.loop import MessageLoop
import time

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "halogen-oxide-225816-facf749e60d7.json"

DIALOGFLOW_PROJECT_ID = 'halogen-oxide-225816'
GOOGLE_APPLICATION_CREDENTIALS = 'halogen-oxide-225816-facf749e60d7.json'
SESSION_ID = 'proyectodasiucm'


class Chatbot():
    chatBotRules = None
    meli = None
    userConversation = None
    response = None

    def __init__(self):
        TOKEN = "639639336:AAEQMqogeObn3k0Y9ztD2L-GshGJdzcekr4" # @Santi
        # TOKEN = '894407782:AAHlyE4ko1wbWlj_oU-utzzBI0weSkC-4Pk' # @Gonzalo
        self.bot = telepot.Bot(TOKEN)

        MessageLoop(self.bot, self.manageMessage).run_as_thread()
        print('Listening ...')

        self.chatBotRules = rules.ChatBotRules()
        self.chatBotRules.setBot(self)

        session_client = dialogflowAPI.SessionsClient()
        session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
        self.userConversation = dialogflow.testingDialogflow()

        while 1:
            time.sleep(10)

    def manageMessage(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        self.chat_id = chat_id

        # mensaje del usuario
        self.message = msg

        self.response = self.userConversation.detect_intent_texts(DIALOGFLOW_PROJECT_ID, SESSION_ID, self.message['text'], 'es')
        print(self.response)

        self.chatBotRules.reset()

        if self.response['intent'] != '':
            self.chatBotRules.declare(Fact(intent = self.response['intent']))
        print(self.chatBotRules.facts)

        # ejecutamos el motor de reglas
        self.chatBotRules.run()

        self.bot.sendMessage(self.chat_id, self.response["responseText"])
        """print(self.message['text'])"""

    def contactMercadoLibre(self, chat_id, msg):
        self.meli = mercado_libre.MercadoLibre()
        self.chat_id = chat_id
        meli_answer = self.meli.formatJSON(self.meli.searchProduct(msg))
        if meli_answer[0]:
            message = meli_answer[0]["link"] + "\n"
            message += "Su calificación según los usuarios es " + str(meli_answer[0]["reviews"]["rating_average"]) + "/5"
            message += " de un total de " + str(meli_answer[0]["reviews"]["total"]) + " evaluaciones" + " \n"
            message += "Su precio es de: $" + str(meli_answer[0]["price"])
            self.bot.sendMessage(self.chat_id, message)
            self.bot.sendPhoto(chat_id, meli_answer[0]["photo"]);
            # self.bot.sendMessage(self.chat_id, message, parse_mode= "Markdown")
        else:
            "no hay"
        # self.bot.sendMessage(self.chat_id, meli_answer[0] if meli_answer else 'no hay')
        # self.bot.sendMessage(self.chat_id, msg)
        # self.bot.sendPhoto(chat_id, meli_answer[0]['photo']);

    def responseInsertMovement(self):
        # Insertar información de los movimientos del usuario
        self.bot.sendMessage(self.chat_id, 'AQUI VAN LOS MOVIMIENTOS')

    def responseAccountBalance(self):
        # Dar balance de cuenta al usuario
        self.bot.sendMessage(self.chat_id, 'AQUI VA EL BALANCE')

    def responseBuy(self):
        # AYUDA A COMPRAR
        if self.response["allParams"]:
            self.contactMercadoLibre(self.chat_id, self.response["searchText"])
        # self.bot.sendMessage(self.chat_id, 'AQUI VAN LAS COMPRAS')

if __name__ == '__main__':
    chatbot = Chatbot()
