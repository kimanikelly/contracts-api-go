from src.contract_api import *
from .utils import *


def test_contract_api():

    # Verifies the return type for both endpoints are Dictionaries
    assert(is_dict(token_endpoint()) == True)
    assert(is_dict(ttBank_endpoint()) == True)

    # Returns the keys from both endpoints and converts them to lists
    token_api_keys = dict_keys_to_list(token_endpoint())
    token_addresses_keys = dict_keys_to_list(token_endpoint()["addresses"])

    ttBank_api_keys = dict_keys_to_list(ttBank_endpoint())
    ttBank_addresses_keys = dict_keys_to_list(ttBank_endpoint()["addresses"])

    assert(token_api_keys[0] == "addresses")
    assert(token_api_keys[1] == "abi")
    assert(token_api_keys[2] == "bytecode")
    assert(token_addresses_keys[0] == "rinkeby")
    assert(token_addresses_keys[1] == "goerli")

    assert(ttBank_api_keys[0] == "addresses")
    assert(ttBank_api_keys[1] == "abi")
    assert(ttBank_api_keys[2] == "bytecode")
    assert(ttBank_addresses_keys[0] == "rinkeby")
    assert(ttBank_addresses_keys[1] == "goerli")
