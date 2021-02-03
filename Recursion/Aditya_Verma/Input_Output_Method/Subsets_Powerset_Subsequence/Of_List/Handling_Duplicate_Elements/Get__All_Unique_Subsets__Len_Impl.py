from sys import setrecursionlimit

"""
Note : len base implementation
Here for shortening the input size, we use index
"""


def get_unique_subsets(unique_subsets: set, input, output: str) -> None:
    if len(input) == 0:
        unique_subsets.add(output)  # Ankh band kar ke add, as it will handle duplicity automatically Note
        return

    output_when_chosen = output  # same as the parent Recursive Nodes output
    # To handle case, when output, is "" empty string, and we don't want to have space after "" empty string Notice
    if output == "":
        output_when_did_not_choose = output + str(input[0])
    else:
        output_when_did_not_choose = output + " " + str(input[0])

    shorter_input = input[1:]  # substring from 1st character

    get_unique_subsets(unique_subsets, shorter_input, output_when_chosen)
    get_unique_subsets(unique_subsets, shorter_input, output_when_did_not_choose)


def get_all_unique_list_subsets(arr):
    unique_subsets = set()  # because its a set the order of elements will not be defined Note
    get_unique_subsets(unique_subsets, arr, "")  # Choosing Output to be Empty String
    return unique_subsets


if __name__ == "__main__":
    setrecursionlimit(11000)
    data = [15, 20, 12]  # a list --> now the results, do have the elements separated Notice
    # data = []  # No Element
    # data = [12]  # Only one elementR
    # data = [99, 99]  # having duplicates - Note : Handles Duplicate

    # data = "abc"  # a string
    # data = "aab"  # a string - having duplicates - Note : It Handles duplicates
    print(get_all_unique_list_subsets(data))
