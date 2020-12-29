from sys import setrecursionlimit

"""
# Note : Index base implementation
# Here for shortening the input size, we use index

# This can work with both string and substring
# String will automatically be converted into list_of_char
"""


def get_unique_subsets(unique_subsets: set, input: list, output: str, index: int) -> None:
    if index >= len(input):
        unique_subsets.add(output)  # Ankh band kar ke add, as it will handle duplicity automatically Note
        return

    output_when_chosen = output  # same as the parent Recursive Nodes output
    # To handle case, when output, is "" empty string, and we don't want to have space after "" empty string Notice
    if output == "":
        output_when_did_not_choose = output + str(input[index])
    else:
        output_when_did_not_choose = output + " " + str(input[index])

    get_unique_subsets(unique_subsets, input, output_when_chosen, index + 1)
    get_unique_subsets(unique_subsets, input, output_when_did_not_choose, index + 1)


def get_all_unique_list_subsets(arr) -> set:
    unique_subsets = set()  # Instead of list, we use set Notice : only difference - To handle duplicity
    get_unique_subsets(unique_subsets, arr, "", 0)  # Choosing Output to be Empty String  Notice
    return unique_subsets


if __name__ == "__main__":
    setrecursionlimit(110000)
    data = [15, 20, 12]  # a list --> now the results, do have the elements separated Notice
    # data = []  # No Element
    # data = [12]  # Only one element
    data = [99, 99]  # having duplicates - Note :  Handles Duplicate

    # data = "abc"  # a string
    # data = "aab"  # a string - having duplicates - Note : It Handles duplicates
    print(get_all_unique_list_subsets(data))
