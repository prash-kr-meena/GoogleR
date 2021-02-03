from sys import setrecursionlimit

"""
Time : O(log n)
returns the index of the key, if found otherwise return -1
"""


# Array has to be sorted **
# NOTE : in case of duplicity, it is not guaranteed who's index will be returned

def binary_search(A, key) -> int:
    if A is None or len(A) == 0:  # edge case
        return -1

    left = 0
    right = len(A) - 1

    while left <= right:
        mid = (left + right) // 2

        if A[mid] > key:  # go left
            right = mid - 1
        elif A[mid] < key:  # go right
            left = mid + 1
        else:  # A[mid] == key
            return mid

    return -1


if __name__ == "__main__":
    setrecursionlimit(11000)
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    search_key = 6
    index = binary_search(arr, search_key)

    print("{} \nKey : {} \nIndex : {}".format(arr, search_key, index))

"""
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
search_key = 6

arr = [1, 2, 2, 2, 4, 5]        # 2 as duplicates
search_key = 2

arr = [1, 2, 2, 2, 4, 5, 6, 7, 8, 9, 10]         # 2 as duplicates
search_key = 2
"""
