#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if ord(s) < 97:
            char = ord(s)
        else:
            char = ord(s) - 32
        print("{:c}".format(char), end='')
    print('')
