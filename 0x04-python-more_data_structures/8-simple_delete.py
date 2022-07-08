#!/usr/bin/python3
def simple_delete(a_dictionary, key = ""):
    dic = {}
    for k, v in a_dictionary.items():
        if k != key:
            dic[k] = v
    return (dic)
