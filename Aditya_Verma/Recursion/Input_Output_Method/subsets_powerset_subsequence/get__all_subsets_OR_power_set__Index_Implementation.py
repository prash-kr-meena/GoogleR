from sys import setrecursionlimit

"""
Note : Index base implementation
Here for shortening the input size, we use index

Note : We are not doing, the backward implementation, because of the nature of the problem.
       As in case of subsequences the position matter
       This solution works for subsequences, subset and power_set



This can work with both string and substring
String will automatically be converted into list_of_char


Remember to make the, input-output Diagram before coding it

"""


def get_subsets(all_subsets: list, input: list, output: str, index: int) -> None:
    if index >= len(input):
        all_subsets.append(output)  # Note : adding all the leaf result, "output" to the list
        return

    output_when_chosen = output  # same as the parent Recursive Nodes output
    output_when_did_not_choose = output + str(input[index])

    get_subsets(all_subsets, input, output_when_chosen, index + 1)
    get_subsets(all_subsets, input, output_when_did_not_choose, index + 1)


def get_all_subsets(data) -> list:
    all_subsets = []
    get_subsets(all_subsets, data, "", 0)  # Choosing Output to be Empty String  NOTE
    return all_subsets


if __name__ == "__main__":
    setrecursionlimit(11000)
    # data = [1, 2, 3]  # a list
    # data = "abc"  # a string
    data = "aab"  # a string - having duplicates - Note : Doesn't Handle
    print(get_all_subsets(data))
