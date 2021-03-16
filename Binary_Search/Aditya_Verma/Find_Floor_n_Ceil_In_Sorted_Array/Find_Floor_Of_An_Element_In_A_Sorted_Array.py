from Utils.Array import input_array

"""
The idea of finding the candidate for our result, is similar to that of the problem, 
First_n_Last_Occurrence_In_Sorted_Array of array


For an element E, all the elements that are SMALLER and EQUAL to the E, will form a candidate

Basically we need to find the GREATEST element SMALLER then or equal to key
"""


def find_floor_of_an_element_in_a_sorted_array(A, key):
    n = len(A)
    left = 0
    right = n - 1

    result = -1  # update when find a valid candidate
    while left <= right:
        mid = (left + right) // 2

        if A[mid] == key:
            return A[mid]  # as FLOOR of e is e, if is present in the A

        elif A[mid] < key:
            # update the result (candidate) and move
            if A[mid] > result:  # We need to find the LARGEST candidate
                result = A[mid]

            # now to move more closer to the key, we go to the right
            left = mid + 1

        else:  # A[mid] > key   Not a candidate, go to left for smaller elements
            right = mid - 1

    return result
    # here we are sending, the actual value and not the index, as we do in binary search Notice


if __name__ == '__main__':
    array = input_array()
    target = int(input())
    print(find_floor_of_an_element_in_a_sorted_array(array, target))

"""
1 2 8 10 10 12 19
5
2 << Output


1 2 8 10 10 12 19
20
19 << Output


1 2 8 10 10 12 19
0
-1 << Output
"""
