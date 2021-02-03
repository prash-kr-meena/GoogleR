from sys import setrecursionlimit

"""
Note : Index base implementation
Here for shortening the input size, we use index
"""


def get_unique_subsets(unique_subsets: set, input: list, output: str, index: int) -> None:
    if index >= len(input):
        unique_subsets.add(output)  # Ankh band kar ke add, as it will handle duplicity automatically Note
        return

    output_when_chosen = output  # same as the parent Recursive Nodes output
    output_when_did_not_choose = output + str(input[index])

    get_unique_subsets(unique_subsets, input, output_when_chosen, index + 1)
    get_unique_subsets(unique_subsets, input, output_when_did_not_choose, index + 1)


def get_all_unique_string_subsets(string) -> set:
    unique_subsets = set()
    get_unique_subsets(unique_subsets, string, "", 0)  # Choosing Output to be Empty String  NOTE
    return unique_subsets


if __name__ == "__main__":
    setrecursionlimit(11000)
    data = [15, 20, 12]  # a list --> The results, do not have the elements separated Notice
    # data = []  # No Element
    # data = [12]  # Only one element
    # data = [99, 99]  # having duplicates - Note : Handles Duplicate

    # data = "abc"  # a string
    # data = "aab"  # a string - having duplicates - Note : It Handles duplicates
    print(get_all_unique_string_subsets(data))
