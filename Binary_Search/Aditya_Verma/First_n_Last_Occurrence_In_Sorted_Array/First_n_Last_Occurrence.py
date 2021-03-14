from Binary_Search.Aditya_Verma.First_n_Last_Occurrence_In_Sorted_Array.First_Occurrence_In_Sorted_Array import \
    first_occurrence_in_sorted_array
from Binary_Search.Aditya_Verma.First_n_Last_Occurrence_In_Sorted_Array.Last_Occurrence_In_Sorted_Array import \
    last_occurrence_in_sorted_array
from Utils.Array import input_array

if __name__ == "__main__":
    array = input_array()  # Expected sorted array
    search_key = int(input())
    first_index = first_occurrence_in_sorted_array(array, search_key)
    last_index = last_occurrence_in_sorted_array(array, search_key)

    print("{} \nKey : {} \nFirst Index : {} \nFirst Index : {}".format(array, search_key, first_index, last_index))

"""
[]      # Just put ENTER
1

[1]
1

1 1 1 1 1
1


1 2 2 2 4 5 6 7 8 9 10
2


1 3 5 5 5 5 67 123 125
5


1 3 5 5 5 5 67 123 125
67
"""
