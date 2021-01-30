import random

from Utils.Array import input_array

"""
inplace implementation of Quick sort
as we are not creating new array, but operating on the same one by its indexes
"""


def randomize_pivot(A, left, right):
    random_index_in_range = random.randrange(left, right + 1)  # as we want to include the last array element too

    # Our logic implementation consider element at last index as the pivot element
    # swapping the elements at the right_most_index with random_index_in_range
    A[right], A[random_index_in_range] = A[random_index_in_range], A[right]
    # Right now our pivot is at index right  NOTE <<


def partition(A, left, right):
    """
    Its task is do the partition and return the pivot_index

    1.  Select a pivot index
        Randomized for better performance [average O(n log n)] , else O(n2)
    2.  partition the array over that pivot_index
    3.  return the pivot_index
    """
    randomize_pivot(A, left, right)

    # NOTE : Right now our actual_pivot is at index right
    future_correct_pivot_index = left  # let say
    actual_pivot_value = A[right]

    while left < right:  # going till the adjacent element of right
        if A[left] < actual_pivot_value:
            A[left], A[future_correct_pivot_index] = A[future_correct_pivot_index], A[left]
            future_correct_pivot_index += 1

        left += 1

    # swapping the actual_pivot to its correct_index
    A[future_correct_pivot_index], A[right] = A[right], A[future_correct_pivot_index]
    return future_correct_pivot_index


# -> Inplace changes to the array A, no need to return A back
def quicksort(A, left, right):
    if left >= right:  # traversal complete
        return

    pivot_index = partition(A, left, right)
    quicksort(A, left, pivot_index - 1)  # sort the left of pivot_index
    quicksort(A, pivot_index + 1, right)  # sort the right of pivot_index


if __name__ == "__main__":
    arr = input_array()
    quicksort(arr, left=0, right=len(arr) - 1)
    print(arr)

"""
12 3 5 7 4 19 26        # random
9 8 7 6 5 4 3 2 1       # reverse sorted
1 2 3 4 5 6 7 8 9 10    # sorted
"""
