# Time  : O(n)
# Space : O(1)
def two_pointer(A):
    left = 0
    right = len(A) - 1

    while left < right:
        if A[left] < 0:  # -ve
            left += 1  # go right

        if A[right] >= 0:  # +ve
            right -= 1  # go left

        if A[left] >= 0 and A[right] < 0:  # left is -Ve and right is +Ve
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    arr = [-12, 11, -13, -5, 6, -7, 5, -3, 11]
    two_pointer(arr)
    print(arr)

"""
[-12, 11, -13, -5, 6, -7, 5, -3, 11]
[-1, 2, -3, 4, 5, 6, -7, 8, 9]
[2, 3, -1, -4, -6]                          # Reverse
[4, 3, 2, 1, 0, -1, -2, -3]                 # Reverse
"""
