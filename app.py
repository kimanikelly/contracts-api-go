from .contract_api import *
from flask import Flask
app = Flask(__name__)


@app.route("/token")
def token():
    return token_endpoint()


@app.route("/ttBank")
def ttBank():
    return ttBank_endpoint()
