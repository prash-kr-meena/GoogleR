from sys import setrecursionlimit

"""
Note : Index base implementation
Here for shortening the input size, we use index

Note : We are not doing, the backward implementation, because of the nature of the problem.
       As in case of subsequences the position matter
       This solution works for subsequences, subset and power_set



This can work with both string and list (array), but for list() there could be different way to print 
String will automatically be converted into list_of_char


Remember to make the, input-output Diagram before coding it

"""


def print_subsets(input: str, output: str, index: int) -> None:
    if index >= len(input):
        print('"' + output + '"')
        return

    output_when_chosen = output  # same as the parent Recursive Nodes output
    output_when_did_not_choose = output + str(input[index])
    # For list, spaces are preferred in output, while for string space in the middle is not preferred  << Notice

    print_subsets(input, output_when_chosen, index + 1)
    print_subsets(input, output_when_did_not_choose, index + 1)


def print_all_string_subsets(data):
    print_subsets(data, "", 0)  # Choosing Output to be Empty String  NOTE
    pass


if __name__ == "__main__":
    setrecursionlimit(11000)

    # data = [1, 2, 3]  # a list
    # data = [15, 20, 12]  # a list --> it works the the results, do not have the elements separated Notice, it's output

    # data = "abc"  # a string
    data = "aab"  # a string -- having duplicates - Note : code is not designed to handle
    print_all_string_subsets(data)
