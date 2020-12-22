from Aditya_Verma.Recursion.Input_Output_Method.subsets_powerset_subsequence.get__all_subsets_OR_power_set__Index_Implementation import \
    get_all_subsets

if __name__ == '__main__':
    string = input()
    subsequences = get_all_subsets(string)
    print(len(subsequences))
    print(subsequences)
