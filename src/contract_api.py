import requests


def token_endpoint():

    return requests.get("http://ec2-34-203-42-249.compute-1.amazonaws.com/token").json()


def ttBank_endpoint():
    return requests.get("http://ec2-34-203-42-249.compute-1.amazonaws.com/ttBank").json()
