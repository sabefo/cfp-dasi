# coding=utf-8
import json
import mercado_libre
import pprint
import requests
import telepot
from telepot.loop import MessageLoop
import time
import urllib


class Chatbot():
    TOKEN = "639639336:AAEQMqogeObn3k0Y9ztD2L-GshGJdzcekr4"
    meli = None

    def manageMessage(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        self.chat_id = chat_id
        self.meli = mercado_libre.MercadoLibre()
        meli_answer = self.meli.formatJSON(self.meli.searchProduct(msg['text']))
        self.bot.sendMessage(self.chat_id, meli_answer if meli_answer else 'no hay')
        # self.bot.sendMessage(self.chat_id, msg['text'])
        # self.bot.sendPhoto(chat_id, meli_answer[0]['photo']);

    def __init__(self):
        super(Chatbot, self).__init__()

        self.bot = telepot.Bot(self.TOKEN)
        print("getting updates")
        MessageLoop(self.bot, self.manageMessage).run_as_thread()

        while True:
            time.sleep(5)


if __name__ == '__main__':
    chatbot = Chatbot()
