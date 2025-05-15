from flask import Flask, render_template, request
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
import os

load_dotenv()

google_key = os.getenv("GOOGLE_API_KEY")
groq_key = os.getenv("GROQ_API_KEY")

google_bot = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", api_key=google_key, temperature=0)
deep_bot = ChatGroq(api_key=groq_key, temperature=0, model="deepseek-r1-distill-llama-70b")
llama_bot = ChatGroq(api_key=groq_key, temperature=0, model="meta-llama/llama-4-scout-17b-16e-instruct")



app = Flask(__name__)
chat_history = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/explore')
def explore():
    return render_template('explore.html')

@app.route('/gemini', methods=['GET', 'POST'])
def gemini():
    if request.method == 'POST':
        user_input = request.form['user_input']
        chat_history.append({'type': 'user', 'text': user_input})

        bot_response = google_bot.invoke(user_input).content
        chat_history.append({'type': 'bot', 'text': f"Gemini Said: {bot_response}"})
    return render_template('gemini.html', chat_history=chat_history)

@app.route('/deepseek', methods=['GET', 'POST'])
def deepseek():

    if request.method == 'POST':
        user_input = request.form['user_input']
        chat_history.append({'type': 'user', 'text': user_input})

        bot_response = deep_bot.invoke(user_input).content
        chat_history.append({'type': 'bot', 'text': f"DeepSeek said: {bot_response[17:]}"})
    return render_template('deepseek.html', chat_history=chat_history) 

@app.route('/llama', methods=['GET', 'POST'])
def llama():
    if request.method == 'POST':
        user_input = request.form['user_input']
        chat_history.append({'type': 'user', 'text': user_input})

        bot_response = llama_bot.invoke(user_input).content
        chat_history.append({'type': 'bot', 'text': f"LLaMA Response: {bot_response}"})
    return render_template('llama.html', chat_history=chat_history)

if __name__ == '__main__':
    app.run(debug=True)
