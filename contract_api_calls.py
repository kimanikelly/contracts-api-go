import requests


def token_endpoint():

    return requests.get("https://smart-contracts-api-node.herokuapp.com/token").json()


def ttBank_endpoint():
    return requests.get("https://smart-contracts-api-node.herokuapp.com/ttBank").json()
