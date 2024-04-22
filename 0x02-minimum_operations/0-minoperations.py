#!/usr/bin/python3
"""Module for minoperations."""


def minOperations(n):
    """`minOperations` calculates the minimum number of operations
    required to obtain exactly `n` occurrences of the character 'H'.
    """
    # All outputs should have a minimum of two characters,
    # including the "Copy All => Paste" sequence.
    if (n < 2):
        return 0
    operations, root = 0, 2
    while root <= n:
        # If `n` is evenly divisible by the square root of `n`, then...
        if n % root == 0:
            # The total number of even divisions by the square root,
            #of `n` is equal to the total number of operations.
            operations += root
            # Set `n` to the remainder of the division.
            n = n / root
            # Reduce the square root to find the remaining smaller values that evenly divide `n`.
            root -= 1
        # Increment the square root until it evenly divides `n`.
        root += 1
    return operations
