# coding=utf-8
import json
import pprint
import requests
import telepot
from telepot.loop import MessageLoop
import time
import urllib


class Chatbot():
    def __init__(self):

        # self.createDatabase()

        # TOKEN = '571166195:AAFEEM3SbBGrSUnsodId-q8TwRQ-yQ3ANOk'  # @eatbotMariabot
        TOKEN = '894407782:AAHlyE4ko1wbWlj_oU-utzzBI0weSkC-4Pk'  # @eatbot_bot

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

        print(self.message['text'])
       



if __name__ == '__main__':
    chatbot = Chatbot()
