from Aditya_Verma.Recursion.Input_Output_Method.Subsets_Powerset_Subsequence.Of_List.Not_Handling_Duplicate_Elements.Print__All_Subsets__Idx_Impl import \
    print_all_list_subsets
from Utils.Array import input_array


def subset_of_array(arr) -> list:
    return print_all_list_subsets(arr)  # To handle duplicate : call get_all_unique_list_subsets(arr) & print it
    # Just before using the above method, remove the " symbol in the base case Notice


if __name__ == '__main__':
    n = int(input())
    array = input_array()
    subset_of_array(array)
