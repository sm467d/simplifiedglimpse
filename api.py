import os
from flask import Flask, request, jsonify
from glimpse import Glimpse

app = Flask(__name__)

# Instantiate the Glimpse object with your API key
api_key = os.environ.get('OPENAI_API_KEY') # Read the API key from the environment variable
glimpse = Glimpse(api_key)


@app.route('/get_transcript', methods=['POST'])
def get_transcript():
    video = request.json['video']
    result = glimpse.get_transcript(video)
    if type(result) == int:
        return jsonify({"error": "YouTubeRequestFailed", "status": result}), result
    return jsonify({"transcript": result})

@app.route('/get_blog', methods=['POST'])
def get_blog():
    transcript = request.json['transcript']
    result = glimpse.get_blog(transcript)
    if type(result) == str:
        return jsonify({"error": "OpenAIRequestFailed", "message": result}), 400
    return jsonify({"blog": result})

@app.route('/get_glimpse', methods=['POST'])
def get_glimpse():
    video = request.json['video']
    status, result = glimpse.get_glimpse(video)
    if status != 399:
        return jsonify({"error": "RequestFailed", "status": status}), status
    return jsonify({"glimpse": result})

if __name__ == "__main__":
    app.run(debug=True)
