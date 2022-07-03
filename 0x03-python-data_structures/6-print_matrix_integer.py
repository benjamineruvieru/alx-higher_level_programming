#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for column in matrix:
        for num in column:
            print('{:d}'.format(num), end='')
        print('')
