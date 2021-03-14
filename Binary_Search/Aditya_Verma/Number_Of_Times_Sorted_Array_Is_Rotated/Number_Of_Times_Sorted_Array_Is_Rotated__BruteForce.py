from Utils.Array import input_array

"""
Important Question

Brute Force :
    1. sort the array
    2. choose an element, and find its index in both the array
    3. take there absolute difference

Time : O(n lg n)
space = O(n)
"""


def find_no_of_times_sorted_array_is_rotated__brute_force(arr) -> int:
    if arr is None or len(arr) == 0:
        return 0

    sorted_array = sorted(arr)

    # choosing 0th element of the sorted_array, ie the smallest element of the array
    # finding its index in the original array
    chosen_element = sorted_array[0]
    difference = None

    for idx, element in enumerate(arr):
        if element == chosen_element:
            difference = abs(idx - 0)  # as our chosen element (the smallest) has index 0
            break  # Essentially our answer is, basically the index of the smallest element in the rotated

    return difference


"""
As of now we have stabilised, that to find the no_of_times_the_array_is_rotated
we basically need to  find the index of the smallest element in the rotated array

We don't need to sort the array, and then find the difference of the two elements
we can just find the index of the minimum element in the rotated array

Time : O(n)
space = O(1) 
"""


def find_no_of_times_sorted_array_is_rotated__brute_force_better(arr):
    if arr is None or len(arr) == 0:
        return 0

    minimum = float("inf")
    minimum_elements_idx = None
    for idx, element in enumerate(arr):
        if element < minimum:
            minimum_elements_idx = idx
            minimum = element

    return minimum_elements_idx


if __name__ == '__main__':
    array = input_array()
    print(find_no_of_times_sorted_array_is_rotated__brute_force(array))
    print(find_no_of_times_sorted_array_is_rotated__brute_force_better(array))

"""
15 18 2 3 6 12
2 << Output

7 9 11 12 5
4 << Output

7 9 11 12 15
0 << Output


[]     ## Just Hit Enter
0 << Output


1     ## Array with single element
0 << Output
"""
