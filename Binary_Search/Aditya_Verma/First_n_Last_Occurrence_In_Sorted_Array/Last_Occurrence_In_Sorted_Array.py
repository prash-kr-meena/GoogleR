from Utils.Array import input_array


def last_occurrence_in_sorted_array(A, key) -> int:
    n = len(A)
    left = 0
    right = n - 1

    result = -1  # if no last occurrence found return -1       # CHANGE from Simple BS NOTICE

    while left <= right:
        mid = (left + right) // 2

        if A[mid] < key:  # go right
            left = mid + 1
        elif A[mid] > key:  # go right
            right = mid - 1
        else:
            # A[mid] == key
            # We can't directly return, mid index as there could more occurrence of key, in the left of index mid
            result = mid  # CHANGE from Simple BS NOTICE
            left = mid + 1

    return result
