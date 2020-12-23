import bisect

# binary search in python using bisect module

sorted_elements = ['A', 'B', 'C', 'D']
print(bisect.bisect_left(sorted_elements, 'B'))

sorted_elements = ['A', 'B', 'C', 'D']
print(bisect.bisect_left(sorted_elements, 'A1'))
print(bisect.bisect_left(sorted_elements, 'E'))

sorted_elements = ['A', 'B', 'C', 'D']
print(bisect.bisect_left(sorted_elements, 'B'))

sorted_elements = ['A', 'B', 'C', 'C', 'C', 'D']
print(bisect.bisect_left(sorted_elements, 'C'))
print(bisect.bisect_right(sorted_elements, 'C'))

sorted_elements = ['A', 'B', 'C', 'C', 'C', 'D']
l = bisect.bisect_left(sorted_elements, 'C')
r = bisect.bisect_right(sorted_elements, 'C')
print(r - l)  # To get the total no of occurrences NOTE


def find_index(elements, value) -> int:
    index = bisect.bisect_left(elements, value)
    if index < len(elements) and elements[index] == value:
        return index
    # else:
    #     return -1  # Item is not present there,


sorted_elements = ['A', 'B', 'C', 'C', 'C', 'D']
bisect.insort_left(sorted_elements, "B1")
bisect.insort_right(sorted_elements, 'C1')
print(sorted_elements)

# importing "bisect" for bisection operations
li = [1, 3, 4, 4, 4, 6, 7]

print("The rightmost index to insert : ", end="")
print(bisect.bisect(li, 4))

print("The leftmost index to insert : ", end="")
print(bisect.bisect_left(li, 4))

print("The rightmost index to insert : ", end="")
print(bisect.bisect_right(li, 4, 0, 4))
#
#
# ---------------------------------------------
#
li1 = [1, 3, 4, 4, 4, 6, 7]
li2 = [1, 3, 4, 4, 4, 6, 7]
li3 = [1, 3, 4, 4, 4, 6, 7]

# using insort() to insert 5 at appropriate position inserts at 6th position
bisect.insort(li1, 5)

print("List after inserting, using insort() : ")
print(li1)

# using insort_left() to insert 5 at appropriate position inserts at 6th position
bisect.insort_left(li2, 5)

print("List after inserting, using insort_left() : ")
print(li2)

# using insort_right() to insert 5 at appropriate position inserts at 5th position
bisect.insort_right(li3, 5, 0, 4)

print("List after inserting, using insort_right() : ")
print(li3)
