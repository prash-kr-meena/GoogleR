import random

from Utils.Array import input_array

"""
https://www.geeksforgeeks.org/quickselect-algorithm/
"""


def randomize_pivot(A, left, right):
    random_index_in_range = random.randrange(left, right + 1)
    # swap it with my actual considered pivot at the rightmost index
    A[right], A[random_index_in_range] = A[random_index_in_range], A[right]
    # with this now, a randomly chosen element becomes pivot on the right most index


"""
    FCPI = future_correct_pivot_index

     FCPI
      |
      v                  |
    .--------------------------.
    [ 1   3   5   4   6  |  2  ]
    '--------------------------'
      ^                  |  ^
      |                  |  |
    Left   ===========>  | Right

    move from left to right (2nd last element), comparing with the pivot ie, A[right]
    and updating the future_correct_pivot_index, so that in the end we can put the pivot there
"""


# Note :  The partition process is exactly the same that is being used in the quicksort process,
#         so you don't need to code anything new there
#         The only thing different is how it recurse and uses this pivot_index returned by the partition process

def partition(A, left, right):
    randomize_pivot(A, left, right)
    future_correct_pivot_index = left
    while left < right:
        if A[left] < A[right]:  # A[right] -> actual_pivot_value
            A[left], A[future_correct_pivot_index] = A[future_correct_pivot_index], A[left]
            future_correct_pivot_index += 1
        left += 1

    # put the actual pivot to its correct position
    A[right], A[future_correct_pivot_index] = A[future_correct_pivot_index], A[right]
    return future_correct_pivot_index


"""
Assuming if k was 1_index_base, then this method is receiving k-1
some basic checks, like  0 >= k <= arr_size, before calling this function
      ie the element asked should be in the range of the array, are ASSUMED


One more ASSUMPTION : all elements in arr[] are distinct
--> As this algorithm doesn't work with duplicate elements

k is the kth (0 indexed) element that, I want to find
kth_element_in_sorted_sense --> Basically kth smallest element in the array
"""


def quick_select(A, left, right, k):
    # Edge cases - Assumed checks
    if left > right:
        print("no kth element found")
        return -1  # no kth element found
    if not (0 <= k <= len(A) - 1):
        print("k is not in the range of the actual array")
        return -1  # k is not in the range of the actual array
    # - - - - - - - - - -

    pivot_index = partition(A, left, right)

    if pivot_index == k:  # found
        return A[pivot_index]
    elif pivot_index < k:
        return quick_select(A, pivot_index + 1, right, k)
    else:
        return quick_select(A, left, pivot_index - 1, k)


if __name__ == "__main__":
    arr = input_array()
    for _ in range(len(arr)):  # put high no in range to see the edge cases
        num = quick_select(arr, left=0, right=len(arr) - 1, k=_)
        print(num)

"""
1 3 5 4 6 2             # random
12 3 5 7 4 19 26        # random
9 8 7 6 5 4 3 2 1       # reverse sorted
1 2 3 4 5 6 7 8 9 10    # sorted
1 2 3 4 1 2 3 4 9 10    # random duplicates -- CHECK IT OUT
"""
