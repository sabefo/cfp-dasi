# coding=utf-8
import json
import mercado_libre
import pprint
import requests
import telepot
from telepot.loop import MessageLoop
import time
import urllib
import dialogflow_v2 as dialogflowAPI
import dialogflow
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "halogen-oxide-225816-facf749e60d7.json"

DIALOGFLOW_PROJECT_ID = 'halogen-oxide-225816'
GOOGLE_APPLICATION_CREDENTIALS = 'halogen-oxide-225816-facf749e60d7.json'
SESSION_ID = 'proyectodasiucm'

class Chatbot():
    #TOKEN = "639639336:AAEQMqogeObn3k0Y9ztD2L-GshGJdzcekr4" # @Santi
    meli = None

    def __init__(self):
        self.eatBotRules.setBot(self)
        TOKEN = '894407782:AAHlyE4ko1wbWlj_oU-utzzBI0weSkC-4Pk' # @Gonzalo
        session_client = dialogflowAPI.SessionsClient()
        session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
        self.userConversation = dialogflow.testingDialogflow()
        self.bot = telepot.Bot(TOKEN)
        MessageLoop(self.bot, self.manageMessage).run_as_thread()
        print('Listening ...')


        # Keep the program running.
        while 1:
            time.sleep(10)

    def manageMessage(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        self.chat_id = chat_id

        # mensaje del usuario
        self.message = msg

        response = self.userConversation.detect_intent_texts(DIALOGFLOW_PROJECT_ID,SESSION_ID,self.message['text'],'es')
        self.bot.sendMessage(self.chat_id, response["responseText"])
        if response["intent"] == "Compra" and response["allParams"]:
            self.contactMercadoLibre(self.chat_id,response["searchText"])

        """print(self.message['text'])"""

    def contactMercadoLibre(self, chat_id,msg):
        self.meli = mercado_libre.MercadoLibre()
        self.chat_id = chat_id
        meli_answer = self.meli.formatJSON(self.meli.searchProduct(msg))
        if meli_answer[0]:
            self.bot.sendMessage(self.chat_id, meli_answer[0]["link"])
        else:
            "no hay"
        # self.bot.sendMessage(self.chat_id, meli_answer[0] if meli_answer else 'no hay')
        # self.bot.sendMessage(self.chat_id, msg)
        # self.bot.sendPhoto(chat_id, meli_answer[0]['photo']);


if __name__ == '__main__':
    chatbot = Chatbot()
