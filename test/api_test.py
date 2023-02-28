from src.contract_api import *


def test_contract_api():

    # Verifies the return type for both endpoints are Dictionaries
    assert(type(token_endpoint()) is dict)
    assert(type(ttBank_endpoint()) is dict)

    # Returns the keys from both endpoints and converts them to lists
    token_api_keys = list(token_endpoint().keys())
    ttBank_api_keys = list(ttBank_endpoint().keys())

    assert(token_api_keys[0] == "addresses")
    assert(token_api_keys[1] == "abi")
    assert(token_api_keys[2] == "bytecode")

    assert(ttBank_api_keys[0] == "addresses")
    assert(ttBank_api_keys[1] == "abi")
    assert(ttBank_api_keys[2] == "bytecode")
