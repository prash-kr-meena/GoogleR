from Binary_Search.Aditya_Verma.First_n_Last_Occurrence_In_Sorted_Array.First_Occurrence_In_Sorted_Array import \
    first_occurrence_in_sorted_array
from Binary_Search.Aditya_Verma.First_n_Last_Occurrence_In_Sorted_Array.Last_Occurrence_In_Sorted_Array import \
    last_occurrence_in_sorted_array
from Utils.Array import input_array


def count_elements_in_sorted_array(A, key):
    first_index = first_occurrence_in_sorted_array(A, element)

    if first_index == -1:  # No element is present
        return 0

    last_index = last_occurrence_in_sorted_array(A, element)

    print("{} \nKey : {} \nFirst Index : {} \nFirst Index : {}"
          .format(A, element, first_index, last_index))

    return last_index - first_index + 1


if __name__ == "__main__":
    array = input_array()  # Expected sorted array
    element = int(input())
    print("count : ", count_elements_in_sorted_array(array, element))

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
