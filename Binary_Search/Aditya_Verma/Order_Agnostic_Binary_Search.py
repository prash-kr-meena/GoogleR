"""
Given a sorted array of numbers, find if a given number ‘key’ is present in the array.
Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order.
"""
from Binary_Search.Algorithm.Binary_Search_Iterative import binary_search
from Binary_Search.Algorithm.Binary_Search_Reverse_Sorted_Array import binary_search_reverse_sorted_array
from Utils.Array import input_array


def order_agnostic_binary_search(A, key) -> int:
    if A is None or len(A) == 0:
        return -1

    if len(A) == 1:
        return 0 if A[0] == key else -1  # only one element, so if it is the key return index 0 else return -1

    # Apply Binary Search on the basis of order
    if A[0] <= A[1]:  # Increasing Order
        return binary_search(A, key)
    else:  # Decreasing Order : Reversely Sorted
        return binary_search_reverse_sorted_array(A, key)


if __name__ == "__main__":
    array = input_array()
    search_key = int(input())
    index = order_agnostic_binary_search(array, search_key)

    print("{} \nKey : {} \nIndex : {}".format(array, search_key, index))

"""
[]      -> Just put enter
[3]
"""

"""                                 ----- Ascending -----
 1 2 3 4 5 6 7 8 9
 6
 
# 2 as duplicates   -   Index Not Guaranteed
1 2 2 2 4 5 6 7 8 9 10
2
"""

"""                                 ----- Descending -----
 9 8 7 6 5 4 3 2 1
 6

# 2 as duplicates   -   Index Not Guaranteed
10 9 8 7 6 5 4 2 2 2 1
2
"""
