"""
This module provides emotion detection via a remote NLP API.

It defines a function `emotion_detector` that returns emotion scores
for a given input string using IBM Watson's EmotionPredict service.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")

@app.route("/emotionDetector", methods=['GET', 'POST'], strict_slashes=False)

def sent_analyzer():
    """
    Handles the /emotionDetector/ endpoint.

    Retrieves text input, calls emotion_detector, and returns
    emotion analysis results or appropriate error messages.
    """

    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    print(f"Input text: {text_to_analyze}")

    if not text_to_analyze:
        return "Invalid text! Please try again!", 400

    # For POST requests (if applicable), get input from form data
    if not text_to_analyze and request.method == 'POST':
        text_to_analyze = request.form.get('textToAnalyze')

    #to check input in logs
    print(f"Received input text: {text_to_analyze}")

    if text_to_analyze is None or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!", 400

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    print(f"Emotion detector response: {response}")

    if response is None:
        return "Invalid text! Please try again.", 400

    # Extract the emotion scores from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']

    # Create emotion dictionary to find dominant emotion
    emotions = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }
    print(f"Emotions extracted: {emotions}")

    # Filter emotions to keep only those with non-None values
    valid_emotions = {k: v for k, v in emotions.items() if v is not None}

    if not valid_emotions:
        return "Invalid text! Please try again."

    dominant_emotion = max(valid_emotions, key=valid_emotions.get)
    dominant_score = valid_emotions[dominant_emotion]

    # Return a formatted string with the sentiment label and score
    return (
        f"For the given statement, the system response is:\n"
        f"- Anger: {anger:.3f}\n"
        f"- Disgust: {disgust:.3f}\n"
        f"- Fear: {fear:.3f}\n"
        f"- Joy: {joy:.3f}\n"
        f"- Sadness: {sadness:.3f}\n\n"
        f"The dominant emotion is {dominant_emotion} with a score of {dominant_score:.3f}."
    )

@app.route("/")
def render_index_page():
    """
    Handles the output to the index.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
