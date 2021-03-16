from Utils.Array import input_array

"""
The idea of finding the candidate for our result, is similar to that of the problem, 
First_n_Last_Occurrence_In_Sorted_Array of array


For an element E, all the elements that are GREATER and EQUAL to the E, will form a candidate

Basically we need to find the SMALLEST element GREATER then or equal to key
"""


def find_ceil_of_an_element_in_a_sorted_array(A, key):
    n = len(A)
    left = 0
    right = n - 1

    result = float("inf")  # update when find a valid candidate
    while left <= right:
        mid = (left + right) // 2

        if A[mid] == key:
            return A[mid]  # as CEIL of e is e, if is present in the A

        elif A[mid] > key:
            # update the result (candidate) and move
            if A[mid] < result:  # We need to find the SMALLEST candidate
                result = A[mid]
            # Now to move more closer to the key, we go to the left
            right = mid - 1

        else:  # A[mid] < key   Not a candidate, go to right for larger elements
            left = mid + 1

    if result == float("inf"):
        return -1

    return result
    # here we are sending, the actual value and not the index, as we do in binary search Notice


if __name__ == '__main__':
    array = input_array()
    target = int(input())
    print(find_ceil_of_an_element_in_a_sorted_array(array, target))

"""
1 2 8 10 10 12 19
5
8 << Output


1 2 8 10 10 12 19
20
-1 << Output


1 2 8 10 10 12 19
0
1 << Output
"""
