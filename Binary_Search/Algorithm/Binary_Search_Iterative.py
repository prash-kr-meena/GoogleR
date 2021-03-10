from Utils.Array import input_array

# Array has to be sorted ** NOTE : in case of duplicity, it is not guaranteed who's index will be returned

"""
Time : O(log n)
returns the index of the key, if found otherwise return -1
"""


def binary_search_within_index(A, key, left, right) -> int:
    if A is None or len(A) == 0:  # edge case
        return -1

    while left <= right:
        mid = (left + right) // 2

        if A[mid] > key:  # go left
            right = mid - 1
        elif A[mid] < key:  # go right
            left = mid + 1
        else:  # A[mid] == key
            return mid

    return -1  # Not returned yet


def binary_search(A, key) -> int:
    return binary_search_within_index(A, key, 0, len(A) - 1)


if __name__ == "__main__":
    array = input_array()
    search_key = int(input())
    index = binary_search(array, search_key)

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
