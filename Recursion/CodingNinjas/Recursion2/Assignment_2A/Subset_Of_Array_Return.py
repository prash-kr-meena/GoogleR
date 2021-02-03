from Recursion.Aditya_Verma.Input_Output_Method.Subsets_Powerset_Subsequence.Of_List.Not_Handling_Duplicate_Elements.Get__All_Subsets__Idx_Impl import \
    get_all_list_subsets
from Utils.Array import input_array
from Utils.Matrix import print_matrix


def subset_of_array(arr) -> list:
    return get_all_list_subsets(arr)  # To handle duplicate : call get_all_unique_list_subsets(arr) & print it


if __name__ == '__main__':
    n = int(input())
    array = input_array()
    print_matrix(subset_of_array(array))
