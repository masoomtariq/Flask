from flask import Flask, render_template, request

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

        chat_history.append({'type': 'bot', 'text': f"Gemini Said: {user_input}"})
    return render_template('gemini.html', chat_history=chat_history)

@app.route('/openai', methods=['GET', 'POST'])
def openai():

    if request.method == 'POST':
        user_input = request.form['user_input']
        chat_history.append({'type': 'user', 'text': user_input})
        chat_history.append({'type': 'bot', 'text': f"OpenAI said: {user_input}"})
    return render_template('openai.html', chat_history=chat_history)

@app.route('/llama', methods=['GET', 'POST'])
def llama():
    if request.method == 'POST':
        user_input = request.form['user_input']
        chat_history.append({'type': 'user', 'text': user_input})
        chat_history.append({'type': 'bot', 'text': f"LLaMA Response: {user_input}"})
    return render_template('llama.html', chat_history=chat_history)

if __name__ == '__main__':
    app.run(debug=True)
