from Utils.Array import input_array


# Time  : O(n)
# Space : O(n)
def rearrange(A):
    temp = []

    for num in A:
        if num < 0:
            temp.append(num)
    for num in A:
        if num >= 0:
            temp.append(num)

    # copy it back
    for i in range(len(A)):
        A[i] = temp[i]


if __name__ == "__main__":
    arr = input_array()
    rearrange(arr)
    print(arr)

"""

-1 2 -3 4 5 6 -7 8 9
2 3 -1 -4 -6                       # Reverse
4 3 2 1 0 -1 -2 -3                 # Reverse containing 0
"""
