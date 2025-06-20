from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    text = request.get_json().get("text")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    result = emotion_detector(text)

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text

if __name__ == "__main__":
    app.run(debug=True)
