#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = []
    for rows in matrix:
        tmp = []
        for nums in rows:
            tmp.append(nums**2)
        newmatrix.append(tmp)
    return newmatrix
