from sys import setrecursionlimit

"""
Distinct Permutation is pending 

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
    for choice in choices:
        updated_output = output + choice
        updated_choices = choices.copy()  # New Copy choices
        updated_choices.remove(choice)  # Update Choices
        permutation(updated_choices, updated_output)


def print_permutation(string) -> None:
    # To represent choices, we could use string, list, tuple or a set
    # With set : we will not be able to handle duplicate elements in our input
    # - You might think, it will give you unique permutation
    # But actually it will not, as you will have less elements in the choices
    unique_choices = set(string)
    permutation(unique_choices, "")


if __name__ == '__main__':
    setrecursionlimit(11000)
    input_string = "abc"
    # input_string = "aaa"  # Wrong output, as other 'a' were not considered
    # input_string = "bbaaa123"  # Same above reason
    print_permutation(input_string)
