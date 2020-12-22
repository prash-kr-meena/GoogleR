# Not doing the brute force, easy implementation
# Already mentioned in Notion


from bisect import bisect_right


# Here, matrix was only row sorted
def find_min_and_max(A):
    # finding the min and max, efficiently, comparing the first elements of all rows & last element of all rows
    minimum = float("inf")
    maximum = float("-inf")
    for row in A:
        size = len(row)
        minimum = min(row[0], minimum)
        maximum = max(row[size - 1], maximum)
    return minimum, maximum


def count_total_elements_smaller_or_equal(A, key):
    # count the total number of elements, that are smaller_or_equal to the Key
    total_elements___smaller_or_equal_to___key = 0
    for row in A:
        elements___smaller_or_equal_to___key___in_this_array = bisect_right(row, key)
        total_elements___smaller_or_equal_to___key += elements___smaller_or_equal_to___key___in_this_array
    return total_elements___smaller_or_equal_to___key


# This Kth is 1 based indexing
def find_kth_element__in__row_wise_sorted_matrix(matrix, k):
    if k < 0 or k > len(matrix) * len(matrix[0]):  # edge cases
        return None

    """
    so the range of numbers to apply binary search is  minimum and maximum
                                                          ^           ^
                                                        left        right
    eg. say minimum=2 & maximum=9, then we are applying the binary search over the range 2 3 4 ... 8 9
        and it doesn't matter if these numbers are present in the array or not
    """
    left, right = find_min_and_max(matrix)  # minimum, maximum

    # operations = 0
    while left < right:  # Notice : breaking when left == right
        mid = (left + right) // 2  # Middle number in the range of counting

        # find the count of elements that are smaller then mid
        total_such_elements = count_total_elements_smaller_or_equal(matrix, mid)

        if total_such_elements < k:  # Idea: if we are looking for kth element, then k-1 numbers will be smaller then it
            left = mid + 1  # go right
        else:
            right = mid  # go left

        # operations += 1
        # print("operations ", operations)      # Operations will remain constant, as for a fixed integer size
        # even though in python there is no limit on the numbers in int,
        # but even then it is going to be finite in other programming lang, and for practical purposes

    return left  # or right


if __name__ == "__main__":
    matrix = [[1, 10, 100],
              [20, 200, 2000],
              [300, 3000, 9000]]
    k = 9
    print(find_kth_element__in__row_wise_sorted_matrix(matrix, k))

    """

    [[16, 28, 60, 64],
    [22, 41, 63, 91],
    [27, 50, 87, 93],
    [36, 78, 87, 94 ]]
    """
