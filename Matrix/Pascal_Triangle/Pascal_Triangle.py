from Utils.Matrix import print_matrix

"""
Google Docs : https://docs.google.com/document/d/11EzTzksWc929SXEBTMwAYCMigWVNKn8NQfigWpyK1JQ/edit#heading=h.cw5ky7ytzanv
Pascal's Triangle 1 - (LeetCode) https://leetcode.com/problems/pascals-triangle/
Pascal's Triangle - (GFG) https://www.geeksforgeeks.org/pascal-triangle/

Q Pascal Triangle 1
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
eg.
Input: 5               Output: [
                                       [1],
                                      [1,1],
                                     [1,2,1],
                                    [1,3,3,1],
                                   [1,4,6,4,1]
                               ]
NOTE: In Pascal's triangle, each number is the sum of the two numbers directly above it.
"""

"""
Approach : Dynamic Programming
    Although the algorithm is very simple, 
    the iterative approach to constructing Pascal's triangle can be classified as dynamic programming because
    we construct each row based on the previous row.
"""


# n : is 1 based indexing
def generate_pascal_triangle(n) -> list[list]:
    triangle: list[list] = []
    zero_th_row = [1]
    triangle.append(zero_th_row)

    for i in range(1, n):  # start from 1th row
        previous_row = triangle[i - 1]
        length_of_previous_row = len(previous_row)

        new_row: list = [None] * (length_of_previous_row + 1)
        new_row[0] = 1  # as we know the first and last element will be 1
        new_row[-1] = 1

        for idx, element in enumerate(new_row):
            if element is None:  # as for first and last, elements are already updated to 1
                new_row[idx] = previous_row[idx - 1] + previous_row[idx]

        triangle.append(new_row)  # adding this new row in the triangle

    return triangle


if __name__ == '__main__':
    number_of_rows = int(input())
    pascal_triangle = generate_pascal_triangle(number_of_rows)
    print_matrix(pascal_triangle)

"""
5
10
"""
