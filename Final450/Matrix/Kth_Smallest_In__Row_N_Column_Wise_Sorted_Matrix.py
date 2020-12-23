# Not doing the brute force, easy implementation
from Final450.Matrix.kth_smallest__in_row_wise_sorted_matrix import find_kth_element__in__row_wise_sorted_matrix

# Note: An optimization suggestion
"""
The code for this problem is ditto, with  find_kth_element__in__row_wise_sorted_matrix(matrix, k):

and by calling the function, we will get correct result
But there is a slight optimization that should be done to that method, 

The finding of minimum and maximum
in the    find_kth_element__in__row_wise_sorted_matrix(matrix, k):     The matrix was only sorted row wise
Whereas, 
in this question it is sorted in both row and column wise
so we can do it in O(1) time   ---> see the below implementation <Its been Tested>
"""


# If the matrix is both row & column wise, sorted
# minimum = Matrix[0][0]  &
# maximum = Matrix[R-1][C-1]            R = len(Matrix)         C = len(Matrix[0])
def find_min_and_max(A):
    R, C = len(A), len(A[0])
    minimum = A[0][0]
    maximum = A[R - 1][C - 1]
    return minimum, maximum


if __name__ == "__main__":
    matrix = [[1, 10, 100],
              [20, 200, 2000],
              [300, 3000, 9000]]
    k = 2
    print(find_kth_element__in__row_wise_sorted_matrix(matrix, k))

    """

    [[16, 28, 60, 64],
    [22, 41, 63, 91],
    [27, 50, 87, 93],
    [36, 78, 87, 94 ]]
    """
