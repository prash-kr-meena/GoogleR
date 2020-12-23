from Aditya_Verma.Recursion.Input_Output_Method.Subsets_Powerset_Subsequence \
    .Of_String.Not_Handling_Duplicate_Characters.Print__All_Subsets__Idx_Impl import print_all_string_subsets
from Utils.Array import input_array


def subset_of_array(arr) -> None:
    print_all_string_subsets(arr)


if __name__ == '__main__':
    n = int(input())
    arr = input_array()
    subset_of_array(arr)
