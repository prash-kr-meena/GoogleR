from Utils.Array import print_array_inline, input_array


# Time: O(n + m)
# Space: O(n + m)
def merge_2_sorted_arrays(A, B) -> list:
    C = []  # Array will have size len(A+B)

    a = b = 0  # pointers in array A and B

    # while either one of them is exhausted
    while a < len(A) and b < len(B):
        if A[a] < B[b]:
            C.append(A[a])
            a += 1
        else:
            C.append(B[b])
            b += 1

    # if B is exhausted then put all the elements of A
    while a < len(A):
        C.append(A[a])
        a += 1

    # if A is exhausted then put all the elements of B
    while b < len(B):
        C.append(B[b])
        b += 1

    return C


if __name__ == "__main__":
    arrA = input_array()
    arrB = input_array()
    # arrA = [1, 1, 5, 5, 10]
    # arrB = [- 1, 0, 0, 1, 1, 8]
    arr = merge_2_sorted_arrays(arrA, arrB)
    print_array_inline(arr)

"""
arrA = 1  3  5  7  9
arrB = 0  2  4  6  8

arrA =  1  1  5  5  10
arrB = -1  0  0  1   1  8
"""
