#!/usr/bin/python3
"""
Define `island_perimeter` to calculate the perimeter of an island in a grid.
"""

border_4 = set()
border_3 = set()
border_2 = set()
border_1 = set()


def edges(grid, i, j):
    """Find cells with either 4, 3, 2 or 1 exposed boundary and add them to
       appropriate set
       Args:
           grid (list): 2d list
           i (int): row number
           j (int): column number
    """
    edges = 0
    try:
        if i == 0:
            edges += 1
        elif grid[i-1][j] == 0:
            edges += 1
    except:
        edges += 1
    try:
        if grid[i+1][j] == 0:
            edges += 1
    except:
        edges += 1
    try:
        if grid[i][j+1] == 0:
            edges += 1
    except:
        edges += 1
    try:
        if j == 0:
            edges += 1
        elif grid[i][j-1] == 0:
            edges += 1
    except:
        edges += 1

    if edges == 1:
        border_1.add((i, j))
    elif edges == 2:
        border_2.add((i, j))
    elif edges == 3:
        border_3.add((i, j))
    elif edges == 4:
        border_4.add((i, j))


def island_perimeter(grid):
    """
    Determine and return the perimeter of the island in the given grid.
    The grid is a rectangular array where 0 represents water and 1 represents land.
    Each cell is a square with a side length of 1.
    There is only one island in the grid.
    Arguments:
        grid (list): A 2D list of integers, either 0 or 1.
    Return:
       int: The perimeter of the island.
    """
    if grid == []:
        return 0
    l = len(grid)
    w = len(grid[0])
    for i in range(l):
        for j in range(w):
            if grid[i][j] == 1:
                edges(grid, i, j)
                if len(border_4) != 0:
                    return 4
    perimeter = (len(border_3) * 3) + (len(border_2) * 2) + (len(border_1))
    return perimeter
