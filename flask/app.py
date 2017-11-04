from flask import Flask, redirect, render_template, request, url_for
app = Flask(__name__)

# Add code here! 
 
if __name__ == '__main__':
    port = 5000
    app.debug = True
    app.run(host='0.0.0.0', port=port)
