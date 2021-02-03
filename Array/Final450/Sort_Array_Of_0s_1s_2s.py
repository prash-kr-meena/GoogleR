from Utils.Array import input_array

ZERO, ONE, TWO = 0, 1, 2


# Time  -> O(n)
# Space -> O(1)  inplace
def sort_by_counting(A):
    cnt_0 = cnt_1 = cnt_2 = 0

    # Count the number of 0s, 1s and 2s in the array
    for num in A:
        if num == ZERO:
            cnt_0 += 1
        elif num == ONE:
            cnt_1 += 1
        elif num == TWO:
            cnt_2 += 1

    # Update the array
    i = 0

    # Store all the 0s in the beginning
    while cnt_0 > 0:
        A[i] = 0
        i += 1
        cnt_0 -= 1

    # Then all the 1s
    while cnt_1 > 0:
        A[i] = 1
        i += 1
        cnt_1 -= 1

    # Finally all the 2s
    while cnt_2 > 0:
        A[i] = 2
        i += 1
        cnt_2 -= 1


if __name__ == "__main__":
    A = input_array()
    sort_by_counting(A)
    print(A)

"""
2 1 0 1 2 0 0 0 1 2 2 2 1 1
1 1 1 1
2 1 0 2 1 0
2 1 0
"""
