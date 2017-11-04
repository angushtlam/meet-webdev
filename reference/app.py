from flask import Flask, redirect, render_template, request, url_for
app = Flask(__name__)

notes = []


@app.route('/helloworld')
def index():
    return 'Hello World'


@app.route('/search')
def search():
    return redirect('https://google.com/')


@app.route('/', methods=['GET'])
def get_notes():
    return render_template('index.html', notes=notes)


@app.route('/', methods=['POST'])
def submit_note():
    text = request.form['text']

    notes.append(text)
    
    return redirect(url_for('get_notes'))
 
 
if __name__ == '__main__':
    port = 5000
    app.debug = True
    app.run(host='0.0.0.0', port=port)
