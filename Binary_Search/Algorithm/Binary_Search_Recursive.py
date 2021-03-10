from sys import setrecursionlimit

from Utils.Array import input_array

# Array has to be sorted ** NOTE : in case of duplicity, it is not guaranteed who's index will be returned

"""
Time : O(log N)
Returns the index of the key, if found otherwise return -1
"""


def binary_search(A, key, left, right) -> int:
    if left > right:
        return -1  # Exhausted the array

    mid = (left + right) // 2

    if A[mid] < key:
        return binary_search(A, key, mid + 1, right)  # search right
    elif A[mid] > key:
        return binary_search(A, key, left, mid - 1)  # search left
    else:
        return mid  # A[mid] == key:


def binary_search_recursive(nums, kay) -> int:
    return binary_search(nums, kay, 0, len(nums) - 1)


if __name__ == "__main__":
    setrecursionlimit(11000)
    array = input_array()
    search_key = int(input())
    index = binary_search_recursive(array, search_key)

    print("{} \nKey : {} \nIndex : {}".format(array, search_key, index))

"""
 1 2 3 4 5 6 7 8 9
 6

# 2 as duplicates   -   Index Not Guaranteed
1 2 2 2 4 5
2

# 2 as duplicates   -   Index Not Guaranteed
1 2 2 2 4 5 6 7 8 9 10
2
"""
