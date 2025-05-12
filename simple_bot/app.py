from flask import Flask, render_template, request, jsonify
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
import os

load_dotenv()

google_key = os.getenv("GOOGLE_API_KEY")

google = ChatGoogleGenerativeAI(model = "learnlm-2.0-flash-experimental", api_key=google_key, temperature=0)

app = Flask(__name__)

chat_history = []

@app.route('/', methods=['GET', 'POST'])
def index():
    global chat_history
    if request.method == 'POST':
        user_input = request.form['user_input']
        chat_history.append({'type': 'user', 'text': user_input})
        
        # Example bot response
        bot_response = f"You said: {user_input}"
        bot_response = google.invoke(user_input).content
        chat_history.append({'type': 'bot', 'text': bot_response})

    return render_template('index.html', messages=chat_history)



app.run(debug=True)
