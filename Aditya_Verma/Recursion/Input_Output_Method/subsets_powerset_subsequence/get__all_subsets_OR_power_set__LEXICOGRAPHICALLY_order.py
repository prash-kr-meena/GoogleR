from Aditya_Verma.Recursion.Input_Output_Method.subsets_powerset_subsequence.get__all_subsets_OR_power_set__Index_Implementation import \
    get_all_subsets

if __name__ == "__main__":
    # data = [1, 2, 3]  # a list
    # data = "abc"  # a string
    data = "aab"  # a string - having duplicates - Note : Doesn't Handle

    subsets = get_all_subsets(data)
    print(type(subsets))
    print(subsets, "<- Unsorted")
    subsets.sort()
    print(subsets, "<- Sorted")
