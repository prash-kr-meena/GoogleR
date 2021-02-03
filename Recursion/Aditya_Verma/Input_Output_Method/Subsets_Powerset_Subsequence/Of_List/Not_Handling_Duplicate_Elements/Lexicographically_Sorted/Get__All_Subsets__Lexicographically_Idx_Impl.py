from sys import setrecursionlimit

from Recursion.Aditya_Verma.Input_Output_Method.Subsets_Powerset_Subsequence.Of_List.Not_Handling_Duplicate_Elements.Get__All_Subsets__Idx_Impl import \
    get_all_list_subsets


def get_all_lexicographically_sorted_list_subsets(arr):
    subsets = get_all_list_subsets(arr)

    print(type(subsets))  # we can't directly sort a set, we first need a list to sort
    print(subsets, "<- Unsorted")
    subsets.sort()
    print(subsets, "<- Sorted")

    return subsets


if __name__ == "__main__":
    setrecursionlimit(11000)

    # data = [15, 20, 12]  # a list --> Now the results, have the elements separated Notice
    data = [99, 99]  # a list - having duplicates - Note : Does not Handle duplicates
    # data = []  # a list

    # data = "abc"  # a string
    # data = "aaa"  # a string - having duplicates - Note : Does not Handle duplicates

    get_all_lexicographically_sorted_list_subsets(data)
