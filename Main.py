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

# Applying custom Sorting

# Nested list of student's info in a Science Olympiad
# List elements: (Student's Name, Marks out of 100, Age)
participant_list = [
    ('Alison', 50, 18),
    ('Terence', 75, 12),
    ('David', 75, 20),
    ('Jimmy', 90, 22),
    ('John', 45, 12)
]

# sorting on the basis of their age
sorted_by_age = sorted(participant_list, key=lambda student_element: student_element[2])
print(sorted_by_age)

# sorting on the basis of their marks
sorted_by_marks = sorted(participant_list, key=lambda student_element: student_element[1])
print(sorted_by_marks)

# sorting on the basis of their names
sorted_by_name = sorted(participant_list, key=lambda student_element: student_element[0])
print(sorted_by_name)

print("\nFinding if a number is already present in the set")
unique_set = {1, 2, 3, 4, 5}
print(unique_set)
print(1 in unique_set)

# you can check that by the in operator, before adding it
if 3 not in unique_set:
    print("adding because did not found 3")
else:
    print("Already present in the set")
