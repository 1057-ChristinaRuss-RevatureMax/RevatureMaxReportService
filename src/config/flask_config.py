from flask import Flask

app = Flask(__name__)


@app.route("/")
def example():
    return "<p>Hello, Flask</p>"