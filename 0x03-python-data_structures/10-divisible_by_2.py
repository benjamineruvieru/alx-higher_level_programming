#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for num in my_list:
        new_list += [True if num % 2 == 0 else False]
    return new_list
