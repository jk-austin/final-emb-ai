import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json = myobj, headers=header)
    
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    #extract emotion scores from the parsed response
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']

    #identify dominant emotion
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)
    dominant_score = emotions[dominant_emotion]


    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant emotion': dominant_emotion,
        'dominant emotion score': dominant_score
    }
