from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')  # the route that calls the following function
def home():
    return render_template('index.html', name='Kokoro')

