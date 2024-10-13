from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests

app = Flask(__name__)
CORS(app)  # This will allow all domains to access the API

#The / route is a basic endpoint that listens for GET requests.
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Chat API"}), 200

#/api/chat listens for POST requests.
@app.route('/api/chat', methods=['POST'])
def chat():
    # Get data from the POST request
    data = request.get_json()
    user_prompt = data.get('prompt')

    if not user_prompt:
        return jsonify({"error": "Missing 'prompt' in request body"}), 400

    # Set up Azure OpenAI API information
    endpoint = os.getenv("ENDPOINT_URL", "https://openai-incubator1.openai.azure.com/")
    deployment = os.getenv("DEPLOYMENT_NAME", "gpt-35-turbo")
    api_key = os.getenv('API_KEY')

    if not api_key:
        return jsonify({"error": "API_KEY environment variable is not set"}), 500

    # Set up headers and request data
    headers = {
        "api-key": api_key,
        "Content-Type": "application/json"
    }

    payload = {
        "messages": [
            {"role": "system", "content": "You are an AI that helps generate business scaling strategies."},
            {"role": "system", "content": "You name from now is Scaling helper."},
            {"role": "user", "content": user_prompt}
        ],
        "max_tokens": 1000,
        "temperature": 0.7
    }

    # Make the request to the Azure OpenAI API
    try:
        response = requests.post(
            f"{endpoint}/openai/deployments/{deployment}/chat/completions?api-version=2024-05-01-preview",
            headers=headers,
            json=payload
        )

        response.raise_for_status()  # Raise an exception for non-200 status codes
        completion = response.json()
        return jsonify({"response": completion['choices'][0]['message']['content']})

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
