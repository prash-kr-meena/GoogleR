from Aditya_Verma.Recursion.Input_Output_Method.Subsets_Powerset_Subsequence.Of_String.Not_Handling_Duplicate_Characters.Get__All_Subsets__Idx_Impl import \
    get_all_string_subsets

if __name__ == '__main__':
    string = input()
    subsequences = get_all_string_subsets(string)
    print(len(subsequences))
    print(subsequences)
