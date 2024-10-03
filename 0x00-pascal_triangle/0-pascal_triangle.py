#!/usr/bin/env python3

"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows in Pascal's Triangle to generate.

    Returns:
        List[List[int]]: A list of lists representing Pascal's Triangle,
        where each inner list is a row of the triangle.
    """
    triangle = []

    if n > 0:
        for row_num in range(1, n + 1):
            row = []
            value = 1
            for col_num in range(1, row_num + 1):
                row.append(value)
                value = value * (row_num - col_num) // col_num
            triangle.append(row)

    return triangle
