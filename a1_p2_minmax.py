# Course: CS261 - Data Structures
# Student Name: Corey Cunningham
# Assignment: Assignment 2: Min-Max
# Description: Create a function that returns a tuple with (min, max) that doesn't use python min or python max


def min_max(arr: []) -> ():
    """
    Returns a tuple with min, max of an array of integers without using built in python functions
    :param arr: list of integers
    :returns tuple (min, max)
    """
    # return None, None if array is empty
    if not arr:
        return None, None

    # set min and max to first element in array
    my_min = my_max = arr[0]
    # loop through array[1] to array[length - 1] change min, max accordingly
    for i in arr[1:]:
        if i < my_min:
            my_min = i
        if i > my_max:
            my_max = i
    return my_min, my_max


# BASIC TESTING
if __name__ == "__main__":
    # example 1
    print(min_max([1, 2, 3, 4, 5]))

    # example 2
    print(min_max([8, 7, 6, -5, 4]))

    # example 3
    print(min_max([]))
