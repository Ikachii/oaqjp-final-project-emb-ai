import requests, json

def emotion_detect(text_to_analyze):
    dom = None
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    myobj = {"raw document" : {"text" : text_to_analyze }}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response =requests.post(url, json = myobj, headers = header)
    f = json.loads(response.text)

    anger_score = f['emotionPredictions'][0]['emotion']['anger']
    disgust_score = f['emotionPredictions'][0]['emotion']['disgust']
    fear_score = f['emotionPredictions'][0]['emotion']['fear']
    joy_score = f['emotionPredictions'][0]['emotion']['joy']
    sadness_score = f['emotionPredictions'][0]['emotion']['sadness']

    mlol = max(anger_score, sadness_score, fear_score, disgust_score, joy_score)
    if response.status_code is 200:
        if mlol is anger_score:
            dom = 'anger'
        elif mlol is sadness_score:
            dom = 'sadness'
        elif mlol is fear_score:
            dom = 'fear'
        elif mlol is disgust_score:
            dom = 'disgust'
        else:
            dom = 'joy'
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dom
    }
