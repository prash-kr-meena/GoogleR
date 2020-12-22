from Aditya_Verma.Recursion.Input_Output_Method.subsets_powerset_subsequence.get__all_UNIQUE_subsets_OR_power_set__Index_Implementation import \
    get_all_unique_subsets

if __name__ == "__main__":
    # data = [1, 2, 3]  # a list
    # data = "abc"  # a string
    data = "aab"  # a string - having duplicates - Note : It Handles duplicates

    subsets_set = get_all_unique_subsets(data)
    print(type(subsets_set))  # we can't directly sort a set, we first need a list to sort

    subsets = list(subsets_set)
    print(subsets, "<- Unsorted")
    subsets.sort()
    print(subsets, "<- Sorted")
