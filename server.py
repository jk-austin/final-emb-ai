from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")

@app.route("/emotionDetector")

def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    
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
    dominant_emotion = max(emotions, key=emotions.get)
    dominant_score = emotions[dominant_emotion]
    
    # Return a formatted string with the sentiment label and score
    return (
        f"For the given statement, the system response is:\n"
        f"- Anger: {anger:.3f}\n"
        f"- Disgust: {disgust:.3f}\n"
        f"- Fear: {fear:.3f}\n"
        f"- Joy: {joy:.3f}\n"
        f"- Sadness: {sadness:.3f}\n\n"
        f"The dominant emotion is **{dominant_emotion}** with a score of **{dominant_score:.3f}**."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    