# Course: CS261 - Data Structures
# Student Name: Corey Cunningham
# Assignment: Assignment 1: Problem 4 Swap Pairs
# Description: Corey Cunningham


def swap_pairs(arr: []) -> []:
    """
    takes an integers and returns a new integer with each pair swapped from original array
    :param arr: array of integers
    :return: array of integers with swapped pairs
    """
    # copy array
    new_arr = list(arr)
    # loop for 0 to length of arr - 1

    # get length of arr
    length = 0
    for _ in new_arr:
        length += 1

    for i in range(length):
        # if the index is odd swap the previous and current index
        if i % 2 != 0:
            new_arr[i - 1], new_arr[i] = new_arr[i], new_arr[i - 1]
    return new_arr


# BASIC TESTING
if __name__ == "__main__":
    # example 1
    print(swap_pairs([1, 2, 3, 4, 5]))

    # example 2
    print(swap_pairs([8, 7, 6, -5, 4, 10]))

    # example 3
    print(swap_pairs([]))
