
#!/usr/bin/python3
"""Provide a function for dividing every element of a numeric matrix.

The function validates the matrix and divisor, then returns a new
matrix containing the results rounded to two decimal places.
"""


def matrix_divided(matrix, div):
    """Divide all matrix elements by div and return a new matrix.

    Args:
        matrix: A non-empty list of equally sized lists of numbers.
        div: An integer or float used to divide each element.

    Returns:
        A new matrix with every result rounded to two decimal places.

    Raises:
        TypeError: If the matrix or divisor has an invalid type,
            or if the matrix rows have different lengths.
        ZeroDivisionError: If the divisor is zero.
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list or not matrix:
        raise TypeError(error)

    for row in matrix:
        if type(row) is not list or not row:
            raise TypeError(error)

        for item in row:
            if type(item) not in (int, float):
                raise TypeError(error)

    row_size = len(matrix[0])

    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [
        [round(item / div, 2) for item in row]
        for row in matrix
    ]
