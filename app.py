from flask import Flask
from transformers import pipeline

app = Flask(__name__)


@app.route("/")
def hello_world():
    r = pipeline("sentiment-analysis")("we love you")
    return f"<p>{r}Hello, flask-github-render!</p>"
