"""
           Left          Right
            |             |
            V             V
Top   -->   1    2    3   4
            5    6    7   8
            9    10  11   12
Bottom --> 13    14  15   16

Output: 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

"""


def print_spiral(A):
    # boundaries
    top = 0
    bottom = len(A) - 1

    left = 0
    right = len(A[0]) - 1

    direction = 0
    while left <= right and top <= bottom:
        if direction == 0:
            """print top row, left -> right"""
            for i in range(left, right + 1):  # for including the last element
                print(A[top][i], end=" ")

            top += 1

        elif direction == 1:
            """print right column, top -> bottom"""
            for i in range(top, bottom + 1):
                print(A[i][right], end=" ")

            right -= 1
        elif direction == 2:

            """print bottom row, right -> left"""
            for i in range(right, left - 1, -1):  # To include the last element we do left-1, also -1 step for i--
                print(A[bottom][i], end=" ")

            bottom -= 1

        elif direction == 3:
            """print lect column, bottom -> top"""
            for i in range(bottom, top - 1, -1):
                print(A[i][left], end=" ")

            left += 1

        direction = (direction + 1) % 4


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    print_spiral(matrix)

"""
matrix = [[1,  2,  3,   4],
          [5,  6,  7,   8],
          [9,  10, 11, 12],
          [13, 14, 15, 16]]

Output: 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 




matrix = [[1,   2,  3,  4,  5,  6],
          [7,   8,  9, 10, 11, 12],
          [13, 14, 15, 16, 17, 18]]
          
Output: 1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11
"""
