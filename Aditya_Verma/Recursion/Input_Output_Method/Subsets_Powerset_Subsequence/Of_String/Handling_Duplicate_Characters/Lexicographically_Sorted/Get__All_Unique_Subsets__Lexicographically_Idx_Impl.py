from Aditya_Verma.Recursion.Input_Output_Method.Subsets_Powerset_Subsequence.Of_String.Handling_Duplicate_Characters.Get__All_Unique_Subsets__Idx_Impl import \
    get_all_unique_string_subsets


def get_all_unique_and_lexicographically_sorted_string_subsets(data):
    subsets = get_all_unique_string_subsets(data)

    print(type(subsets))  # we can't directly sort a set, we first need a list to sort
    subsets = list(subsets)
    print(subsets, "<- Unsorted")
    subsets.sort()
    print(subsets, "<- Sorted")

    return subsets


if __name__ == "__main__":
    # data = [1, 2, 3]  # a list
    # data = [15, 20, 12]  # a list --> it works the the results, do not have the elements separated Notice, it's output

    # data = "abc"  # a string
    data = "aab"  # a string - having duplicates - Note : It Handles duplicates
    get_all_unique_and_lexicographically_sorted_string_subsets(data)
