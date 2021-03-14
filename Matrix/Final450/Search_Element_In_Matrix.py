from Binary_Search._Algorithm.Binary_Search_Iterative import binary_search

"""
Too Brute Force
Time : O(n2)      -> Just literally travelling through the matrix  --> Quadratic
Space : O(1)
"""


def search__brute_force_quadratic(A, target):
    for row_index, row in enumerate(A):
        for index, element in enumerate(row):
            if element == target:
                return True

    return False  # otherwise


# Improving on the fact we, know the ranges in the row
# Time : O(rows + columns)      -> Linear
# Space : O(1)
def search__optimizing_brute_force_linear(A, target):
    for row_index, row in enumerate(A):
        size = len(row)
        if row[0] <= target <= row[size - 1]:  # found the correct row
            for index, element in enumerate(row):
                if element == target:
                    return True

    return False  # otherwise


# Optimizing over, the linear search we do after finding the row
# Time : O(n + log m)   ~  O(n)  ie, Linear
def search__optimizing_linear(A, target):
    for row_index, row in enumerate(A):
        size = len(row)
        if row[0] <= target <= row[size - 1]:  # found the correct row
            index = binary_search(row, target)
            if index >= 0:
                return True

    return False  # otherwise


# Time : O(log N + log M)       , if any one of them is huge then   O(max(log n, log m))
def search__most_optimized_logarithm(A, target):
    if not A:  # case []
        return 0

    rows, columns = len(A), len(A[0])
    if not columns:  # case [[]]
        return 0

    # find the correct row
    correct_row_index = -1
    left, right = 0, rows - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid][0] <= target <= A[mid][columns - 1]:
            correct_row_index = mid
            break
        elif A[mid][0] > target:  # go left
            right = mid - 1
        else:  # go right
            left = mid + 1

    if correct_row_index == -1:
        return False

    # find the correct element in that found row
    index = binary_search(A[correct_row_index], target)
    return index >= 0


""" # vanilla binary search implementation
    left, right = 0, columns - 1
    while left <= right:
        mid = (left + right) // 2
        if A[correct_row_index][mid] == target:
            return True
        elif A[correct_row_index][mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return False
"""

if __name__ == "__main__":
    A = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 2
    print(search__brute_force_quadratic(A, target))
    print(search__optimizing_brute_force_linear(A, target))
    print(search__optimizing_linear(A, target))
    print(search__most_optimized_logarithm(A, target))

"""
Input : matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
Output: true


Input : matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
Output: false


Input : matrix = [], target = 0
Output: false
"""
