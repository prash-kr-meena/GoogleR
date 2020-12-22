print("hello")

# --  updating one array with another array values --
array_one = [2, 3, 4, 5, 6, 7, 8, 9]
array_two = [1, 1, 1, 1, 1]

array_one[0:4] = array_two[0:4]
print(array_one)

# finding a character in a string
str_A = "BACDE"
char = "X"  # Not Present
print(str_A.find(char))  # index of char in A

"""
str_A = "BACDE"
char = "D"

str_A = "CABA"         # case with duplicity -- Important Case
char = "A"

str_A = "BACDE"
char = "X"              # Not Present
"""

# -- lengths in matrix --
matrix = [[1, 2, 3, 4, 5, 6],
          [7, 8, 9, 10, 11, 12],
          [13, 14, 15, 16, 17, 18]]

print(len(matrix))
print(len(matrix[0]))

# appending multiple elements  --> Not possible
a_list = [1, 2, 3, 4, 5]
a_list.append(100)
a_list.append(200)
# a_list.append(300, 500)           # No    -> Error
print(a_list)


# Going in reverse with range
print(list(range(0, 10, -1)))
print(list(range(10, 0, -1)))
