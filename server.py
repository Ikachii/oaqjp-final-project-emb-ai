from flask import Flask, render_template, request
from Emo.Emotion_Detector import emotion_detect

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detect():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detect(text_to_analyze)
    anger = response['anger']
    fear = response['fear']
    joy = response['joy']
    disgust = response['disgust']
    sadness = response['sadness']
    dom = response['dominant_emotion']
    if dom is None:
        return 'Invalid input'
    else:
        return "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}.".format(anger, disgust, fear, joy, sadness, dom)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

