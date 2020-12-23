from sys import setrecursionlimit

from Final450.Array.merge_2_sorted_arrays import merge_2_sorted_arrays

"""
merge_sort
Index based implementation

Time : O(n lg n)
Space : O(1)
"""


def merge(A, left, mid, right):
    # get the first and second array - Which are sorted in themselves
    first_array = A[left:mid + 1]  # including mid
    second_array = A[mid + 1: right + 1]
    third_array = merge_2_sorted_arrays(first_array, second_array)  # returns a sorted array
    '''instead of calling this, you can write it here and directly update the original array A '''

    # updating the original array  -- CRAZY ---
    A[left:right + 1] = third_array[:]  # notice

    '''
    # updating the original array     - NORMAL Way
    i = 0
    while left <= right:
        A[left] = third_array[i]
        i += 1
        left += 1
    '''


def merge_sort(A, left, right):
    if left >= right:  # traversal complete, & one element is sorted when left == right
        return

    mid = (left + right) // 2
    merge_sort(A, left, mid)
    merge_sort(A, mid + 1, right)
    merge(A, left, mid, right)


if __name__ == "__main__":
    setrecursionlimit(110000)
    arr = [12, 3, 5, 7, 4, 19, 26]  # random
    # arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]     # reverse sorted
    # arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # sorted
    merge_sort(arr, left=0, right=len(arr) - 1)
    print(arr)
