"""
Emotion Detector Web Application.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)
@app.route("/emotionDetector")
def sent_detector():
    """
    Module that gets the response typed in and communicates with the function Emotion_detector
    to analyze it
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger_value = response['anger']
    disgust_value = response['disgust']
    fear_value = response['fear']
    joy_value = response['joy']
    sadness_value = response['sadness']
    dominant_emotion_value = response['dominant_emotion']
    if dominant_emotion_value is None:
        return "Invalid text! Please try again!."
    text = ("For the given statement, the system response is "
        "'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} "
        "and 'sadness': {}. The dominant emotion is {}.")
    return text.format(anger_value,disgust_value,fear_value,
                       joy_value,sadness_value,dominant_emotion_value)
@app.route("/")
def render_index_page():
    """
    This renders the basic html website at /
    """
    return render_template("index.html")
if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 5000)
