from flask import Flask, make_response

app = Flask(__name__)


@app.errorhandler(404)
def catch_all(arg):
    return make_response(arg, 404)
