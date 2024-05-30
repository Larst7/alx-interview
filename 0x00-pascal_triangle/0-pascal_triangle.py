#!/usr/bin/python3
"""Module that returns a list of lists of integers
representing Pascal's triangle of n rows."""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n rows.
    
    Args:
        n (int): The number of rows in the Pascal's triangle.
    
    Returns:
        List[List[int]]: Pascal's triangle represented as a list of lists of integers.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # First element is always 1
        if i > 0:
            for j in range(1, i):
                # Compute the inner elements of the row
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)  # Last element is always 1
        triangle.append(row)

    return triangle

