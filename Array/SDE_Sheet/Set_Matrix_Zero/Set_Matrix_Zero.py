from Utils.Matrix import input_matrix, print_matrix

"""
Submitted on LeetCode : https://leetcode.com/problems/set-matrix-zeroes/
google doc : https://docs.google.com/document/d/11EzTzksWc929SXEBTMwAYCMigWVNKn8NQfigWpyK1JQ/edit#

Q Set Matrix Zeroes
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Input:  [   [1,1,1],                 Output: [   [1,0,1],
            [1,0,1],                             [0,0,0],
            [1,1,1]                              [1,0,1]
        ]                                    ]

Input:  [                           Output:[
           [0,1,2,0],                          [0,0,0,0],
           [3,4,5,2],                          [0,4,5,0],
           [1,3,1,5]                           [0,3,1,0]
        ]
"""

"""
Two approaches : 
1. Using Set : storing the x and y coordinate separately, so that at maximum will have O(n+m) space  
2. Constant Space - Dummy Value 
        Kinda like an hack, and only applicable when you know the range of data that can be present in the array
"""

"""
Time  : O(m*n) + O(n*m)  ==> O(n*m)      m & n : are rows and columns
Space : O(m+n) at worst case, when each row and column has 0
"""


# Making rows-columns 0, Inplace
def set_matrix_zero(matrix) -> None:
    zero_value_rows = set()
    zero_value_columns = set()

    # Traverse the matrix, and get the x & y coordinates of 0 value element
    total_rows = len(matrix)
    for i in range(total_rows):
        columns_in_this_row = len(matrix[i])
        for j in range(columns_in_this_row):
            if matrix[i][j] == 0:
                zero_value_rows.add(i)
                zero_value_columns.add(j)

    # print(zero_value_rows, zero_value_columns)

    # For all the zero_value_rows, make all element of that row 0
    for row_idx in zero_value_rows:
        columns_in_this_row = len(matrix[row_idx])
        for j in range(columns_in_this_row):
            matrix[row_idx][j] = 0  # only column changing

    # For all the zero_value_columns, make all element of that column 0
    for column_idx in zero_value_columns:
        no_of_rows = len(matrix)
        for i in range(no_of_rows):
            matrix[i][column_idx] = 0  # only rows changing

    print()


if __name__ == '__main__':
    array_2d = input_matrix()
    print_matrix(array_2d)
    set_matrix_zero(array_2d)
    print_matrix(array_2d)

"""
3
1 1 1
1 0 1
1 1 1
"""

"""
3
0 1 2 0
3 4 5 2
1 3 1 5
"""
