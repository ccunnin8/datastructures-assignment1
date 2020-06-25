# Course: CS261 - Data Structures
# Student Name: Corey Cunningham
# Assignment: Assignment 1 part 1
# Description: A function that receives four inputs: m, n, a, b and determines if numbers between m and n inclusive
#              are divisible by m, n, both or none


def length(s: str) -> int:
    """
    returns the length of a string
    """

    # loop through string and increment count for each character
    count = 0
    for _ in s:
        count += 1
    return count


def is_divisible(m: int, n: int, a: int, b: int) -> []:
    """
    checks if a and b are divisible by [m, n]
    :param m: start
    :param n: end
    :param a: check if number between m and n is divisible by a
    :param b: check if number between m and n is divisible by b
    """
    # check for valid inputs
    if m < 0 or n < 0 or a < 0 or b < 0 or n < m or a == b:
        return "Incorrect input"

    # create header
    header1 = "Num"
    header2 = f"\tDiv by {a} and/or {b}?"
    under1 = "-" * length(header1) + "\t"
    under2 = "-" * length(header2)

    # initialize output array with header and border
    answers = [header1 + header2, under1 + under2]

    # loop backwards from n to m
    for i in range(n, m - 1, -1):
        div_by_a = i % a == 0
        div_by_b = i % b == 0
        if div_by_a and div_by_b:
            answers.append(f"{i}\tboth")
        if not div_by_a and not div_by_b:
            answers.append(f"{i}\tNone")
        if div_by_a and not div_by_b:
            answers.append(f"{i}\tdiv by {a}")
        if div_by_b and not div_by_a:
            answers.append(f"{i}\tdiv by {b}")
    return answers


# BASIC TESTING
if __name__ == "__main__":
    # example 1
    print(*is_divisible(2, 7, 10, 12), sep="\n")

    # example 2
    print(is_divisible(1, 20, -1, 3))
    print(is_divisible(20, 0, 100, 200))
    print(is_divisible(10, 8, 7, 2))
    print(is_divisible(3, 30, 7, 7))
