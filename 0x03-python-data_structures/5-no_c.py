#!/usr/bin/python3
def no_c(my_string):
    new_str = ''
    for str in my_string:
        if str == 'c' or str == 'C':
            continue
        else:
            new_str += str
    return new_str
