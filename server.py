''' Exeecuting this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def emo_detector():
    """
    Detects the emotion of the provided text from the request.

    Retrieves text from the query parameter 'textToDetect', processes it using
    the emotion_detector function, and returns the emotion label and score.

    Returns:
        str: A formatted string describing the emotion label and its score, or
        an error message if the input is invalid.
    """
    # Retrieve the text to detect from the request arguments
    text_to_analyse = request.args.get('textToAnalyze')
    
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyse)
    
    # Initialize the result string
    res = "For the given statement, the system response is"
    
    # Iterate through the response
    emotions = [f" '{key}' : {value}" for key, value in response.items() if key != 'dominant_emotion']
    res += ", ".join(emotions[:-1])  # Join all emotions except the last one with commas
    res += f" and{emotions[-1]}."  # Add 'and' before the last emotion

    # Add the dominant emotion
    res += f" The dominant emotion is <b>{response['dominant_emotion']}</b>."

    return res

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)