from sys import setrecursionlimit

"""
permutation_len & choices is kind of like our input
permutation_len is used to track the number of choices we need to make
Choices : determines what all choices we have
"""


def permutation(choices, output) -> None:
    no_of_choices_to_make = len(choices)

    # Base Case
    if no_of_choices_to_make == 0:
        print(output)
        return

    # Have len(choices) number of choices, (can be 0, 1, 2, ....)
    for i in range(0, len(choices)):
        curr_choice = choices[i]
        updated_output = output + curr_choice
        updated_choices = choices[:i] + choices[i + 1:]  # New choices <String> decrease by 1 size Notice
        permutation(updated_choices, updated_output)


def print_permutation(string) -> None:
    # To represent choices, we could use string, list, tuple or a set
    # With List : It will be able to handle duplicate elements in our input
    # With list comes a bit of responsibility, as it is mutable -> hence need extra care NOTICE
    # One easy way to handle it would be to use a little space and create a copy to pass to downstream recursive calls
    choices = list(string)
    permutation(string, "")


if __name__ == '__main__':
    setrecursionlimit(11000)
    input_string = "abc"
    # input_string = "aaa"  # For duplicate elements, duplicate permutations are shown
    # input_string = "bbaaa123"  # Same above reason
    print_permutation(input_string)
