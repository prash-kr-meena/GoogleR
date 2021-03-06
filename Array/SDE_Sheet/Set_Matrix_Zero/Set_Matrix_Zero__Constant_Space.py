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


def set_matrix_zero(matrix):
    fill_0_in_0th_row = False
    fill_0_in_0th_column = False

    row_count, column_count = len(matrix), len(matrix[0])

    # Find answer to the question ?  fill_0_in_0th_row and fill_0_in_0th_column
    for j in range(column_count):
        if matrix[0][j] == 0:  # going through first row, by changing columns
            fill_0_in_0th_row = True
            break

    for i in range(row_count):
        if matrix[i][0] == 0:  # going through first column, by changing rows
            fill_0_in_0th_column = True
            break

    # Now we are allowed to use the 0th row and 0th column, as space
    # so we can mark the first_element of ith row and first_element of jth column
    # ie, matrix[i][0] = 0       for marking first element of ith row
    # ie, matrix[0][j] = 0       for marking first element of jth column

    # Here you need to start from the 1st row and 1st column, as we are useing 0th row and column :: NOTE
    for i in range(1, row_count):
        for j in range(1, column_count):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # now for all the marked first_elemnets we will make that row zero, basically checking what we have marked above
    # Here you need to start from the 1st row and 1st column, as we are useing 0th row and column :: NOTE
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
