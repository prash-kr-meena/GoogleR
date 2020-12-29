from sys import setrecursionlimit

"""
Note : Index base implementation
Here for shortening the input size, we use index

Note : We are not doing, the backward implementation, because of the nature of the problem.
       As in case of subsequences the position matter
       This solution works for subsequences, subset and power_set


Remember to make the, input-output Diagram before coding it
"""


def get_subsets(all_subsets: list, input: list, output: str, index: int) -> None:
    if index >= len(input):
        all_subsets.append(output)  # # Adding all the leaf result, "output" to the list Note
        return

    output_when_chosen = output  # same as the parent Recursive Nodes output

    # To handle case, when output, is "" empty string, and we don't want to have space after "" empty string Notice
    if output == "":
        output_when_did_not_choose = output + str(input[index])
    else:
        output_when_did_not_choose = output + " " + str(input[index])

    get_subsets(all_subsets, input, output_when_chosen, index + 1)
    get_subsets(all_subsets, input, output_when_did_not_choose, index + 1)


def get_all_list_subsets(arr) -> list:
    all_subsets = []
    get_subsets(all_subsets, arr, "", 0)  # Choosing Output to be Empty String  Notice
    return all_subsets


if __name__ == "__main__":
    setrecursionlimit(11000)

    data = [15, 20, 12]  # a list --> the results, do have the elements separated Notice
    # data = []  # No Element
    # data = [12]  # Only one element
    # data = [99, 99]  # having duplicates - Note : Doesn't Handle

    # data = "abc"  # a string
    # data = "aab"  # a string   having duplicates - Note : Doesn't Handle
    print(get_all_list_subsets(data))
