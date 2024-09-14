import json 
import requests
def emotion_detector(text_to_analyze):
    """
    Sends text to an external API for emotion detection and returns the emotion label and score.

    Args:
        text_to_analyze (str): The text to be analyzed.

    Returns:
        dict: A dictionary containing 'label' and 'score' keys for the emotion detection result.
    """
    # URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Custom header specifying the model ID for the emotion detection service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the emotion detection API
    response = requests.post(url, json=myobj, headers=header, timeout=10)

    json_response = json.loads(response.text)
    # if the response is 200, extract the emotion predictions
    if response.status_code == 200:
        emotion_predictions = json_response["emotionPredictions"][0]["emotion"]
        emotion_predictions['dominant_emotion'] = max(emotion_predictions, key=emotion_predictions.get)
    # if the response is 400 or 500, set the emotion predictions to None
    if response.status_code == 400 or response.status_code == 500:
        # return the dictionary with keys and values set to None
        emotion_predictions = {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion": None}

    return emotion_predictions