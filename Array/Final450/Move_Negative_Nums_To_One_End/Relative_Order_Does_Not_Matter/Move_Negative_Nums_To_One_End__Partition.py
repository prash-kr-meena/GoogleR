from Utils.Array import input_array


# Time  : O(n)
# Space : O(1)

# Basically partition_around_0
def partition_around_0(A, left, right):
    pivot_value = 0
    future_correct_pivot_index = left
    while left <= right:  # Going till the last element and not just to 2nd last
        if A[left] < pivot_value:
            A[left], A[future_correct_pivot_index] = A[future_correct_pivot_index], A[left]
            future_correct_pivot_index += 1

        left += 1
    # Here we don't actually need to put 0 in its correct position,
    # as it was just for reference, It wasn't a pivot that we chose from inside of the array


if __name__ == "__main__":
    arr = input_array()
    partition_around_0(arr, left=0, right=len(arr) - 1)
    print(arr)

"""
-1 2  -3   4   5   6  -7   8  9
2  3  -1  -4  -6                           # Reverse
4  3   2   1   0  -1  -2  -3               # Reverse containing 0
"""
