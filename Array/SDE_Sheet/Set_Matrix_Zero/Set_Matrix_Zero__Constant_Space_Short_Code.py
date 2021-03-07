from Utils.Matrix import input_matrix, print_matrix

"""
Submitted on LeetCode : https://leetcode.com/problems/set-matrix-zeroes/
google doc : https://docs.google.com/document/d/11EzTzksWc929SXEBTMwAYCMigWVNKn8NQfigWpyK1JQ/edit#
"""

"""
Two approaches : 
1. Using Set : storing the x and y coordinate separately, so that at maximum will have O(n+m) space  
2. Constant Space - Dummy Value 
        Kinda like an hack, and only applicable when you know the range of data that can be present in the array
        
        BUT :: Actually this will be of a very high time complexity,                            
            first you will do O(n*m) traversal on the array, to find if this element has 0 value
            then, for that element's row & column you will traverse that row & column to make them 0
            Time Complexity : O(n*m) * O(n+m)  
                                as for each of the matrix element we will traverse the whole row ie O(n)
                                and we will also traverse the whole matrix ie O(m)


    Below method is of O(n*m) time and Constant space
    Youtube : https://www.youtube.com/watch?v=l_9QffkcYkk&ab_channel=Broletscode        <<<<<<<<<<
"""


# You could decrease the no of loops, and do the task of 1st, 2nd and 3rd loop in one go
def set_matrix_zero(matrix):
    row_count, column_count = len(matrix), len(matrix[0])

    fill_0_in_0th_row = False
    fill_0_in_0th_column = False
    # Find answer to the question ?  fill_0_in_0th_row and fill_0_in_0th_column

    # Here you need to start from the 0st row and 0th column, as we are using 0th row and column :: NOTE
    for i in range(0, row_count):
        for j in range(0, column_count):  # here we are string from 0
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

            if i == 0:
                fill_0_in_0th_row = True
            if j == 0:
                fill_0_in_0th_column = True

    # now for all the marked first_elemnets we will make that row zero, basically checking what we have marked above
    # Here you need to start from the 1st row and 1st column, as we are using 0th row and column :: NOTE
    for i in range(1, row_count):
        for j in range(1, column_count):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Now we have done the work of updating the rows and columns to 0 value,  except the 0th row & column
    # so we will use the earlier marked, variables if they had 0's in them then they would be true otherwize false
    if fill_0_in_0th_row:
        for j in range(column_count):
            matrix[0][j] = 0  # going through first row, by changing columns

    if fill_0_in_0th_column:
        for i in range(row_count):  # going through first row, by changing columns
            matrix[i][0] = 0

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
