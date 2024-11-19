import requests
import json

def sentiment_analyzer(text_to_analyse):
    # URL du service d'analyse de sentiment
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'

    # Construction de la charge utile de la requête dans le format attendu
    myobj = { "raw_document": { "text": text_to_analyse } }

    # En-tête personnalisé spécifiant l'ID du modèle pour le service d'analyse de sentiment
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    # Envoi d'une requête POST à l'API d'analyse de sentiment
    response = requests.post(url, json=myobj, headers=header)

    # Analyse de la réponse JSON de l'API
    formatted_response = json.loads(response.text)

    # Extraction de l'étiquette de sentiment et du score de la réponse
    label = formatted_response['documentSentiment']['label']
    score = formatted_response['documentSentiment']['score']

    # Retour d'un dictionnaire contenant les résultats de l'analyse de sentiment
    return {'label': label, 'score': score}