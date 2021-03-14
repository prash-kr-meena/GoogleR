from Search_Sorting._Algorithms.Quick_Select import quick_select
from Utils.Array import input_array

"""
Submitted on LeetCode : https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/


for kth largest in an array, you can just use the QuickSelect implementation
and instead of passing k, you can pass something like arr_size - k -1
"""


def find_kth_largest(arr, k) -> int:
    n = len(arr)
    return quick_select(arr, 0, n - 1, n - k)


if __name__ == '__main__':
    array = input_array()
    k = int(input("k : "))
    print(find_kth_largest(array, k))
    print(sorted(array))

"""
12 3 5 7 19      - Random
1 2 3 4 5 6      - Sorted
9 8 7 6 5 4      - Reverse Sorted
3 3 1 8 2 1      - Random with duplicates 
                   Notice : Wrong Result - doesn't handle duplicity
"""
