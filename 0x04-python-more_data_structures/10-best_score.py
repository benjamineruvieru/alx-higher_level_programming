#!/usr/bin/python3
def best_score(a_dictionary):
    num = 0
    mainkey = "None"
    if a_dictionary:
        for key, value in a_dictionary.items():
            if value > num:
                num = value
                mainkey = key
        return mainkey
    else:
        return 'None'
