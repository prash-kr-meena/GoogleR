from Binary_Search.Aditya_Verma.Number_Of_Times_Sorted_Array_Is_Rotated.Number_Of_Times_Sorted_Array_Is_Rotated import \
    find_index_of_the_minimum_element__in_sorted_rotated_array
from Binary_Search._Algorithm.Binary_Search_Iterative import binary_search_within_index
from Utils.Array import input_array

"""
Submitted on linkedin : https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/

Time : O(log n)
Space : O(1) 
"""


def find_element_in_rotated_sorted_array(arr, key) -> int:
    n = len(arr)
    min_value_idx = find_index_of_the_minimum_element__in_sorted_rotated_array(arr)
    # print("min_value_idx ", min_value_idx)

    if min_value_idx == -1:
        return -1  # Could not find element

    next = (min_value_idx + 1) % n
    prev = (min_value_idx + n - 1) % n  # This can only be done in a rotated sorted array Notice

    if key == arr[min_value_idx]:
        return min_value_idx

    elif arr[0] <= key <= arr[prev]:
        return binary_search_within_index(arr, key, 0, prev)

    elif arr[min_value_idx] <= key <= arr[n - 1]:
        return binary_search_within_index(arr, key, min_value_idx, n - 1)
    else:
        return -1  # "Not present"


if __name__ == '__main__':
    array = input_array()
    target = int(input())
    n = len(array)

    print(find_element_in_rotated_sorted_array(array, target))
"""
15 18 2 3 6 12
15
0 << Output


15 18 2 3 6 12
3
3 << Output

15 18 2 3 6 12
6
4 << Output


-----------------

7 9 11 12 5
5
4 << Output


7 9 11 12 5
9
1 << Output
-----------------

7 9 11 12 15
15
4 << Output


7 9 11 12 15
15
4 << Output

7 9 11 12 15
7
4 << Output

-----------------

[]     ## Just Hit Enter
0 << Output


1     ## Array with single element
0 << Output
"""
