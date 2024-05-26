## app.py
from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')  # HTML file with input form

@app.route('/analyze', methods=['POST'])
def analyze():
    # Extract text from the form submission
    text = request.form['text']
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    # Fetch API endpoint and key from environment variables
    endpoint = os.environ.get("CONTAINER_API_URL")
    api_key = os.environ.get("API_KEY")

    # Ensure required configurations are available
    if not endpoint or not api_key:
        return jsonify({'error': 'API configuration not set'}), 500

    # Construct the full URL for the sentiment analysis API
    url = f"{endpoint}/text/analytics/v3.1/sentiment"
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': api_key  # Replace with the name of the header expected by your API
    }
    body = {
        'documents': [{'id': '1', 'language': 'en', 'text': text}]
    }

    # Make the HTTP POST request to the sentiment analysis API
    response = requests.post(url, json=body, headers=headers)
    if response.status_code != 200:
        return jsonify({'error': 'Failed to analyze sentiment'}), response.status_code

    # Process the API response
    data = response.json()
    results = data['documents'][0]
    detailed_results = {
        'document': text,
        'overall_sentiment': results['sentiment'],
        'confidence_positive': results['confidenceScores']['positive'],
        'confidence_neutral': results['confidenceScores']['neutral'],
        'confidence_negative': results['confidenceScores']['negative']
    }

    # Return the detailed results to the client
    return jsonify({'results': detailed_results})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)