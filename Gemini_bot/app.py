from flask import Flask, render_template, request, jsonify

from langchain_google_genai import ChatGoogleGenerativeAI

google_key = "AIzaSyBDyGNT3OrQMfI8SfH9q0LsyikQgqihqWg"

google = ChatGoogleGenerativeAI(model = "learnlm-1.5-pro-experimental", api_key=google_key, temperature=0)

app = Flask(__name__)

@app.route('/')
def chatbot():-
    return render_template('new.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json.get('message')
    bot_reply = google.invoke(user_message).content
    return jsonify({'reply': bot_reply})

app.run(debug=True)
