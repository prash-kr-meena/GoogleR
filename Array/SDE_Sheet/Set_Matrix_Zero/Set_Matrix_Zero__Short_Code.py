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
# We can write the same code :: Shorter way, instead of 3 loop we can do in 2 loops only NOTICE
def set_matrix_zero(matrix) -> None:
    zero_value_rows = set()
    zero_value_columns = set()

    # as the matrix is not jagged we can find out n & m, easily
    n = len(matrix)
    m = len(matrix[0])  # assuming matrix has 0th row, its not empty or None

    # Traverse the matrix, and get the x & y coordinates of 0 value element
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                zero_value_rows.add(i)
                zero_value_columns.add(j)

    # print(zero_value_rows, zero_value_columns)

    # going through all the matrix element, and where the i or j belongs to our set, we make that matrix element 0
    for i in range(n):
        for j in range(m):
            if i in zero_value_rows or j in zero_value_columns:
                matrix[i][j] = 0

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
