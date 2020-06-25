# Course: CS261 - Data Structures
# Student Name: Corey Cunningham
# Assignment: Problem 5: Camel Case
# Description: Create three functions that work together to convert strings to camel case


def is_char(c: str) -> bool:
    """returns true if character is a-z or A-Z"""
    return 97 <= ord(c) <= 122 or 65 <= ord(c) <= 90


def to_lower(c: str) -> str:
    """ converts a character to lowercase if uppercase or returns original"""
    if 65 <= ord(c) <= 90:
        return chr(ord(c) + 32)
    return c


def to_upper(c: str) -> str:
    """converts a char to uppercase if lowercase or returns original"""
    if 97 <= ord(c) <= 122:
        return chr(ord(c) - 32)
    return c


def capitalize_str(c: str) -> str:
    """ returns a capitalized version of a string"""
    return to_upper(c[0]) + c[1:]


def length(input_string: str) -> int:
    """
    count letters in a string and return count
    """
    count = 0
    for _ in input_string:
        count += 1
    return count


def input_cleanup(input_string: str) -> str:
    """
    strips a string of leading or trailing non characters, converts all characters to lower case, and
    converts inner non characters to underscores
    """

    output = ""
    length_output = 0
    # loop over input string
    for c in input_string:
        # check if character
        if not is_char(c):
            # trip leading non characters by not adding a non character until added char
            if length_output != 0:
                if is_char(output[length_output - 1]):
                    output += "_"
                    length_output += 1
        # if c is a character convert to lower if upper and add to output
        else:
            output += to_lower(c)
            length_output += 1

    # trim trailing
    if length_output != 0:
        while not is_char(output[length_output - 1]):
            output = output[:-1]
            length_output -= 1
    return output


def is_clean_string(input_string: str) -> bool:
    """
    checks whether input string has been cleaned
    """
    return input_string == input_cleanup(input_string)


def camel_case(input_string: str, func_is_clean, func_cleanup):
    """
    takes a non camel case string that has been cleaned and returns the camelCaseVersion
    :param input_string: string to be converted
    :param func_is_clean: function that returns true if str is "clean"
    :param func_cleanup: function that cleans up string
    """
    # sanitize input string
    clean_input = func_cleanup(input_string)     # DO NOT DELETE / CHANGE

    # check if input string is ready for camelCase conversion

    if not func_is_clean(clean_input):           # DO NOT DELETE / CHANGE
        return None                              # DO NOT DELETE / CHANGE

    # check that input string has at least two words in it (has at least 1 separator)
    separator_count = 0
    for i in clean_input:
        if not is_char(i):
            separator_count += 1

    # return None if it does not
    if separator_count < 1:
        return None

    # convert clean input string into camelCase
    separator_index = 0
    output = ""
    for i in range(length(clean_input)):
        if not is_char(clean_input[i]):
            # capitalize words after first word
            if separator_index != 0:
                new_word = capitalize_str(clean_input[separator_index + 1: i])
                separator_index = i
                output += new_word
            # don't capitalize first word
            else:
                output += clean_input[:i]
                separator_index = i
    # add and capitalize last word
    output += capitalize_str(clean_input[separator_index + 1:])
    return output


# BASIC TESTING
if __name__ == "__main__":
    if __name__ == "__main__":
        test_set = ("_random_ _word_provided",
                    "@$ptr*4con_", " ran  dom  word",
                    "example    word   ", "ANOTHER_Word",
                    "__", "_ _ _", "    ", "435%7_$$", "random")

        # example 1
        for test_string in test_set:
            result = input_cleanup(test_string)
            print(length(result), result)
        print()

        # example 2
        for test_string in test_set:
            result = input_cleanup(test_string)
            print(is_clean_string(test_string), is_clean_string(result))
        print()

        # example 3
        for test_string in test_set:
            result = camel_case(test_string, is_clean_string, input_cleanup)
            print("'" + test_string + "'", "-->", result)