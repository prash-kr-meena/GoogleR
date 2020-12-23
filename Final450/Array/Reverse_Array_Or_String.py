# This doesn't actually change the underlying array
# -> returning a new array that is in reverse order
def reverse_pythonic(arr):
    return arr[::-1]


# This is inplace, _ ie modifying the underlying array
def reverse_iterative(arr):
    i, j = 0, len(arr) - 1

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return arr


# This is inplace, _ ie modifying the underlying array
def reverse_recursively_helper(arr, start, end):
    if start >= end:
        return  # traveral complete

    # swap the two extreme elements
    arr[start], arr[end] = arr[end], arr[start]
    reverse_recursively_helper(arr, start + 1, end - 1)


def reverse_recursive(arr):
    if arr is None or len(arr) < 2:
        return arr

    reverse_recursively_helper(arr, 0, len(arr) - 1)
    return arr


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]  # Custom Input
    print(reverse_pythonic(array))
    print(reverse_iterative(array))  # reversed
    print(reverse_recursive(array))  # reversed again -> correct order

    string = 'prashant'  # Custom Input
    string_arr = list(string)
    print(reverse_pythonic(string_arr))
    print(reverse_iterative(string_arr))  # reversed
    print(reverse_recursive(string_arr))  # reversed again -> correct order

''' [1, 2, 3, 4, 5]
    [9, 8, 6, 4, 2]

    'prashant' ->
    "meena"
'''
