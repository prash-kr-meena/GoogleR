from sys import setrecursionlimit
from sys import getrecursionlimit

"""
Array has to be sorted **
NOTE : in case of duplicity, it is not guaranteed who's index will be returned


Time : O(log N)
Returns the index of the key, if found otherwise return -1
"""


# Binary Search Recursion1 -- Reverse
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


def set_recursion_attributes():
    setrecursionlimit(11000)
    print("Updated Recursion1 Limit : ", getrecursionlimit())


if __name__ == "__main__":
    set_recursion_attributes()
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    search_key = 6
    index = binary_search_recursive(arr, search_key)

    print("{} \nKey : {} \nIndex : {}".format(arr, search_key, index))

"""
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
search_key = 6


arr = [1, 2, 2, 2, 4, 5]        # 2 as duplicates
search_key = 2

arr = [1, 2, 2, 2, 4, 5, 6, 7, 8, 9, 10]         # 2 as duplicates
search_key = 2
"""
