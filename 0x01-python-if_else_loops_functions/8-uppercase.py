#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if ord(s) < 97:
            print('{}'.format(s), end='')
            continue
        char = ord(s) - 32
        print("{:c}".format(char), end='')
