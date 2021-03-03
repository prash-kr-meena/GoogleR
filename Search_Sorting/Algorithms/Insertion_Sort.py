from Utils.Array import input_array

"""
Sorting in Natural Order ie, Increasing 
Inplace changes to the array A, no need to return A back
"""


def insertion_sort(A) -> None:
    n = len(A)
    for i in range(1, n):  # going from index 1  Notice
        j = i  # j so that we don't update i

        while j > 0 and A[j - 1] > A[j]:  # previous value is greater then next value
            A[j - 1], A[j] = A[j], A[j - 1]  # swap
            j -= 1  # going back


if __name__ == '__main__':
    arr = input_array()
    insertion_sort(arr)  # Inplace
    print(arr)

"""
4 3 2 1
1 2 3 4
3 2 1 2 3
"""
