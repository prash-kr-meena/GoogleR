from DynamicProgramming.Other.Binomial_Coefficient.Space_N_Time_Efficient_Binomial_Coefficient import \
    space_n_time_efficient_binomial_coefficient
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
Prerequisite :  Binomial_Coefficient__Memoized.py

Approach : Binomial Expansion (Mathematics)

    NOTE :
        Number of entries in every line is equal to the line number.
        For example,
        the first line has “1”,                     1 entry
        the second line has “1 1”,                  2 entries
        the third line has “1 2 1”,.. and so on.    3 entries

    AND
        Every entry in a line is the value of a Binomial Coefficient.
        The value of i’th entry in line number line is C(line, i).

    The value can be calculated using the following combination formula.      nCr
    nCr =    ___n!___       ==>           lineCi =    ___line!____
             r! (n-r)!                                i! (line-r)!


    So we could prefill the map, or  2D array, and then when filling up the actual list we can directly read from the
    memo (map) or 2D array
"""

"""
    Time :  O(n^3) 
            O(n^2) to go through all the elements of the pascal triangle and update there value 
            and O(n) and 

    Space : O(n^2)
"""


# n : is 1 based indexing
def generate_pascal_triangle(n) -> list[list]:
    triangle: list[list[int]] = []
    for line_number in range(0, n):
        new_row: list = [None] * (line_number + 1)
        triangle.append(new_row)
        for i in range(0, len(new_row)):
            new_row[i] = space_n_time_efficient_binomial_coefficient(line_number, i)  # O(line) time

    return triangle


if __name__ == '__main__':
    number_of_rows = int(input())
    pascal_triangle = generate_pascal_triangle(number_of_rows)
    print_matrix(pascal_triangle)

"""
5
10
"""
