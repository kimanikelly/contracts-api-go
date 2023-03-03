from .contract_api_calls import *
from flask import Flask
app = Flask(__name__)


@app.route("/")
def endpoint_directory():
    return {
        "token_endpoint": "/token",
        "ttBank_endpoint": "/ttBank"
    }


@app.route("/token")
def token():
    return token_endpoint()


@app.route("/ttBank")
def ttBank():
    return ttBank_endpoint()
