from Utils.Array import input_array


# Todo : Check if the implementation is correct or not?
#  like have i implemented in the correct way
# Thought : move the min to its correct position
# -> Inplace changes to the array A, no need to return A back
def insertion_sort(A) -> None:
    n = len(A)
    for i in range(n):
        min = A[i]
        min_index = i
        for j in range(i + 1, n):
            if A[j] < min:
                min = A[j]
                min_index = j

        # loop ends - found the min
        A[i], A[min_index] = min, A[i]


if __name__ == '__main__':
    arr = input_array()
    insertion_sort(arr)  # Inplace
    print(arr)

"""
4 3 2 1
1 2 3 4
3 2 1 2 3
"""
