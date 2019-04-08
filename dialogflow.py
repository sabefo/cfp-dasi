import telepot
from telepot.loop import MessageLoop
import dialogflow_v2 as dialogflow

DIALOGFLOW_PROJECT_ID = 'halogen-oxide-225816'
GOOGLE_APPLICATION_CREDENTIALS = 'halogen-oxide-225816-facf749e60d7.json'
SESSION_ID = 'proyectodasiucm'

class testingDialogflow:

	def __init__(self):
		session_client = dialogflow.SessionsClient()
		session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

	def detect_intent_texts(self,project_id, session_id, texts, language_code):
		session_client = dialogflow.SessionsClient()
		session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
		# print('Session path: {}\n'.format(session))
		text_input = dialogflow.types.TextInput(text=texts, language_code=language_code)
		query_input = dialogflow.types.QueryInput(text=text_input)
		response = session_client.detect_intent(session=session, query_input=query_input)
		intentName = response.query_result.intent.display_name
		allParams = response.query_result.all_required_params_present
		fulfillmentText = response.query_result.fulfillment_text
		paramBienes = response.query_result.parameters.fields["Bienes"].string_value
		paramMarca = response.query_result.parameters.fields["Marca"].string_value
		searchFor = paramBienes + " " + paramMarca
		responseDialogFlow = {
		"intent": intentName,
		"allParams": allParams,
		"searchText": searchFor,
		"responseText": fulfillmentText
		}
		# print(searchFor)


		# print(intentName, finalResponse)
		# print('=' * 20)
		# print('Query text: {}'.format(response.query_result.query_text))
		# print('Detected intent: {} (confidence: {})\n'.format(
		# 	response.query_result.intent.display_name,
		# 	response.query_result.intent_detection_confidzence))
		# print('Fulfillment text: {}\n'.format(
		# 	response.query_result.fulfillment_text))
		return responseDialogFlow