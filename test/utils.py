def is_dict(dictionary):
    getType = type(dictionary)

    return getType is dict


def dict_keys_to_list(dict_of_keys):
    toList = list(dict_of_keys.keys())

    return toList
