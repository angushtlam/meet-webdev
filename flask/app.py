from flask import Flask, render_template, request
app = Flask(__name__)


notes = []

@app.route('/', methods=['GET'])
def get_notes():
    return render_template('main.html', notes=notes)

@app.route('/', methods=['POST'])
def submit_note():
    text = request.form['text']
    notes.append(text)
    return render_template('main.html', notes=notes)
