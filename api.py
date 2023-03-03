from .contract_api_calls import *
from flask import Flask
app = Flask(__name__)


@app.route("/")
def endpoint_directory():
    return {
        "/token": "Request the /token endpoint to return the Addresses, ABI, and Bytecode of Token.sol",
        "/ttBank": "Request the /ttBank endpoint to return the Addresses, ABI, and Bytecode of TTBank.sol"
    }


@app.route("/token")
def token():
    return token_endpoint()


@app.route("/ttBank")
def ttBank():
    return ttBank_endpoint()
