from Final450.Matrix.kth_smallest__in_row_wise_sorted_matrix import find_kth_element__in__row_wise_sorted_matrix


def median__row_sorted_matrix(A):
    # obviously handle, edge cases [] and [[]]
    R = len(A)
    C = len(A[0])
    median_index = (R * C + 1) // 2  # 1 based indexing,    n/2 if the total elements were n
    # so median_index - 1      elements will should be smaller then the number which will be the median
    return find_kth_element__in__row_wise_sorted_matrix(A, median_index)


if __name__ == "__main__":
    matrix = [[1, 10, 100],
              [20, 200, 2000],
              [300, 3000, 9000]]
    print(median__row_sorted_matrix(matrix))

    """
    Input:     R = 3, C = 3
               matrix = [[1, 3, 5],
                    [2, 6, 9],
                    [3, 6, 9]]
    Output: 5
    Explanation: Sorting matrix elements gives us  {1,2,3,3,5,6,6,9,9}. Hence, 5 is median.

    Input:     R = 3, C = 1
               matrix = [[1], [2], [3]]
    Output: 2


matrix = [[0, 1, 2, 3, 4],
          [10, 11, 12, 13, 14],
          [20, 21, 22, 23, 24] ]

matrix = [[1, 10, 100],
              [20, 200, 2000],
              [300, 3000, 9000]]

    """
