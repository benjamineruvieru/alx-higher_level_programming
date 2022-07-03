#!/usr/bin/python3
def multiple_returns(sentence):
    result = ()
    if len(sentence) > 0:
        lenght = len(sentence)
        first_cha = sentence[0]
        result = (lenght, first_cha)
    else:
        result = (0, 'None')
    return result
