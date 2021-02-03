from Search_Sorting.Algorithms.Quick_Sort import partition
from Utils.Array import input_array

"""
https://www.geeksforgeeks.org/quickselect-algorithm/
"""

# Not :  The partition process is exactly the same that is being used in the quicksort process,
#         The difference bw the quick_sort & quick_select is the way they uses this pivot_index


"""
One more ASSUMPTION : all elements in arr[] are distinct
--> As this algorithm doesn't work with duplicate elements
"""


# Assuming if k was 1_index_base, then this method is receiving k-1
# 1.  Element asked should be in the range of the array  ie, 0 >= k <= arr_size

# Find kth element
def quick_select(A, left, right, k):  # kth (0 indexed) element that, I want to find
    # Edge cases - Assumed checks
    if left > right:
        print("no kth element found")
        return -1
    if not (0 <= k <= len(A) - 1):
        print("k is not in the range of the actual array")
        return -1

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
