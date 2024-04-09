#!/usr/bin/python3
'''Module for discovering Pascal's Triangle numbers'''


def pascal_triangle(n):
    '''
    Function to generate Pascal's Triangle

    Parameters: n (int): The number of rows of Pascal's
    triangle to generate.

    Returns: A list of lists representing Pascal's Triangle.
    '''
    pascal_triangle = []

    if n <= 0:
        return pascal_triangle

    for row in range(n):
        '''First element is always 1.'''
        new_row = [1]

        '''Fill in the middle elements.'''
        for col in range(1, row):
            new_row.append(pascal_triangle[-1][col-1] + pascal_triangle[-1][col])

        if row > 0:
            new_row.append(1)
            '''Last element is always 1.'''
        pascal_triangle.append(new_row)

    return pascal_triangle
