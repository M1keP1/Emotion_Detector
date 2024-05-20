import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header) 
    if response.status_code == 400:
        return {'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
                }
    formatted_response = json.loads(response.text)
    anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)
    results = { 'anger': anger,
                'disgust': disgust,
                'fear': fear,
                'joy': joy,
                'sadness': sadness,
                'dominant_emotion': dominant_emotion } 
    return results
