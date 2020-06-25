# Course: CS261 - Data Structures
# Student Name: Corey Cunningham
# Assignment: Assignment 1 Part 3: Matrix Add
# Description: Create a function that adds to matrices (2 2-D arrays)


def matrix_add(a: [[]], b: [[]]) -> [[]]:
    """
    sums 2 matrixes and returns the result
    :param a: 2-D array of int
    :param a: 2-D array of int
    :return: a 2-D array of the matrix sum of a and b
    """
    # verify that a and b have the same dimensions
    rows_a = rows_b = cols_a = cols_b = 0
    for _ in a:
        rows_a += 1
    for _ in b:
        rows_b += 1
    for _ in a[0]:
        cols_a += 1
    for _ in b[0]:
        cols_b += 1
    if rows_a != rows_b or cols_a != cols_b:
        return None
    # initialize empty matrix same as size a and b with all 0s
    results = [[0] * cols_a for _ in range(rows_a)]
    # loop through 1-d representation of the matrix converting each index to row and col and adding
    for i in range(rows_a * cols_a):
        row = i // cols_a
        col = i % cols_a
        results[row][col] = a[row][col] + b[row][col]
    return results


# BASIC TESTING
if __name__ == "__main__":
    # example 1
    m1 = [[1, 2, 3], [2, 3, 4]]
    m2 = [[5, 6, 7], [8, 9, 10]]
    m3 = [[1, 2], [3, 4], [5, 6]]

    print(matrix_add(m1, m2))
    print(matrix_add(m1, m3))
    print(matrix_add(m1, m1))
    print(matrix_add([[]], [[]]))
    print(matrix_add([[]], m1))

