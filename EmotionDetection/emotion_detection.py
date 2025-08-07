import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json = myobj, headers=headers)
    
    if not text_to_analyze or text_to_analyze.strip() == "":
        return None

    if response.status_code == 200:
        # Parsing the JSON response from the API, then extract scores
        formatted_response = json.loads(response.text)
        emotions = formatted_response['emotionPredictions'][0]['emotion']  # Extract emotions dictionary
        
        #identify dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)
        dominant_score = emotions[dominant_emotion]
$
        return {
            'anger': emotions.get('anger'),
            'disgust': emotions.get('disgust'),
            'fear': emotions.get('fear'),
            'joy': emotions.get('joy'),
            'sadness': emotions.get('sadness'),
            'dominant_emotion': dominant_emotion,
            'dominant_score': dominant_score
        }

    # If 400, set all to None
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'dominant_score': None
        }