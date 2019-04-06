# coding=utf-8
import json
import pprint
import requests
import telepot
from telepot.loop import MessageLoop
import time
import urllib
import telepot
from telepot.loop import MessageLoop
import dialogflow_v2 as dialogflow

DIALOGFLOW_PROJECT_ID = 'halogen-oxide-225816'
GOOGLE_APPLICATION_CREDENTIALS = 'halogen-oxide-225816-facf749e60d7.json'
SESSION_ID = 'proyectodasiucm'

class Chatbot():
	def __init__(self):
		TOKEN = '894407782:AAHlyE4ko1wbWlj_oU-utzzBI0weSkC-4Pk'  
		session_client = dialogflow_v2.SessionsClient()
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
		self.bot.sendMessage(self.chat_id, response)
		"""print(self.message['text'])"""




if __name__ == '__main__':
	chatbot = Chatbot()
