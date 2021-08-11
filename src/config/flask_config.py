from flask import Flask, make_response
from os import environ

app = Flask(__name__)
app.debug = environ.get("DEBUG", True)


@app.errorhandler(404)
def catch_all(arg):
    return make_response(arg, 404)
