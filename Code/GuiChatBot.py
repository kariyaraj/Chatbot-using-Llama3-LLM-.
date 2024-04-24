# This is a web version of ChatBot.py, which uses Flask to create a web app.

# Importing Libraries
from flask import Flask, render_template, request
import ollama
# Creating the Flask App
app = Flask(__name__)


def generate_response(prompt):
    message = [
        {
            'role': 'system',
            'content': 'You are a helpful assistant.',
        },
        {
            'role': 'user',
            'content': prompt
        }
    ]
    response = ollama.chat(model='llama3', messages=message, stream=False)
    # response = {'message': {'content': 'hi'}}
    # response.headers.add('Access-Control-Allow-Origin', 'http://127.0.0.1:5500')
    # extract_sql_string(response['message']['content'])
    return response['message']['content']
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    # Get Prompt from User
    prompt = request.form['prompt']

    # User can stop the chat by sending 'End Chat' as a Prompt
    if prompt.upper() == 'END CHAT':
        return 'END CHAT'

    # Generate and Print the Response from ChatBot
    response = generate_response(prompt)
    return response

if __name__ == '__main__':
    app.run(debug=True)