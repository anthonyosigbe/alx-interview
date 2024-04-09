#!/usr/bin/python3
'''Module for discovering Pascal's Triangle numbers'''


def pascal_triangle(n):
    '''
    Function to generate Pascal's Triangle

    Parameters:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        pascal_triangle (list): A list of lists representing Pascal's Triangle.
    '''
    pascal_triangle = []

    if n <= 0:
        return pascal_triangle

    # Generate rows.
    for row in range(n):
        new_row = [1]  # First element is always 1.

        # Fill in the middle elements.
        for col in range(1, row):
            new_row.append(pascal_triangle[-1][col-1] + pascal_triangle[-1][col])

        if row > 0:
            new_row.append(1)  # Last element is always 1.
        pascal_triangle.append(new_row)

    return pascal_triangle
