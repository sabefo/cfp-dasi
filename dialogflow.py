# coding=utf-8
import telepot
from telepot.loop import MessageLoop
import dialogflow_v2 as dialogflowAPI

#Credenciales para la conexión entre Python y DialogFlow
DIALOGFLOW_PROJECT_ID = 'halogen-oxide-225816'
GOOGLE_APPLICATION_CREDENTIALS = 'halogen-oxide-225816-facf749e60d7.json'
SESSION_ID = 'proyectodasiucm'

# Clase de DialogFlow para interactuar con la configuración hecha en la nube
class testingDialogflow:
    # Método que inicializa la clase con las claves necesarias obtenidas de Google
    def __init__(self):
        session_client = dialogflowAPI.SessionsClient()
        session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

    # Método que nos dice el intent con el que se va a interactuar, recibe el texto 
    # que mandó el usuario para ser analizado. El método también imprime la información
    # que se genera dentro para facilitar la detección de errores y el seguimiento del 
    # flujo del código. El método regresa un diccionario con el intent detectado, si
    # los parámetros que ese método necesita están presentes, el texto que se va a usar
    # en el método de búsqueda de productos y por último el texto de la respuesta de DialogFlow
    def detect_intent_texts(self, project_id, session_id, texts, language_code):
        session_client = dialogflowAPI.SessionsClient()
        session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
        text_input = dialogflowAPI.types.TextInput(text=texts, language_code=language_code)
        query_input = dialogflowAPI.types.QueryInput(text=text_input)
        response = session_client.detect_intent(session=session, query_input=query_input)
        intentName = response.query_result.intent.display_name
        allParams = response.query_result.all_required_params_present
        fulfillmentText = response.query_result.fulfillment_text
        paramData = response.query_result.parameters
        paramBienes = response.query_result.parameters.fields["Bienes"].string_value
        paramMarca = response.query_result.parameters.fields["Marca"].string_value
        searchFor = paramBienes + " " + paramMarca
        responseDialogFlow = {
            "intent": intentName,
            "allParamsPresent": allParams,
            "paramsData": paramData,
            "searchText": searchFor,
            "responseText": fulfillmentText
        }
        print(searchFor)

        print(intentName)
        print('=' * 20)
        print('Query text: {}'.format(response.query_result.query_text))
        print('Detected intent: {} (confidence: {})\n'.format(
            response.query_result.intent.display_name,
            response.query_result.intent_detection_confidence))
        print('Fulfillment text: {}\n'.format(
            response.query_result.fulfillment_text))
        return responseDialogFlow
