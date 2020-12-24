# Time  : O(n log n)
# Space : O(n)      in worst case : space for the two sub arrays  len(a) + len(b) = n


def modified_merge_logic(A, left, mid, right):
    # get the first and second array - Which are correctly arranged in themselves <here its not sorting related>
    first_array = A[left:mid + 1]  # including mid
    second_array = A[mid + 1: right + 1]

    third_array = []  # with correct arrangement - overall
    # here that arrangement is basically having all -ves before and then all +ves on right side

    # putting all -ve values
    # -> To maintain the order we first do it for first_array and then for second_array
    for num in first_array:
        if num < 0:
            third_array.append(num)

    for num in second_array:
        if num < 0:
            third_array.append(num)

    # putting all -ve values
    # -> To maintain the order we first do it for first_array and then for second_arrays
    for num in first_array:
        if num >= 0:  # including 0's
            third_array.append(num)

    for num in second_array:
        if num >= 0:  # including 0's
            third_array.append(num)

    # Updating the original array
    A[left:right + 1] = third_array[:]  # or  third_array[0: len(third_array)]


# NOTE : this implementation is exact same, except we are calling the modified merge_logic
def merge_sort(A, left, right):
    if left >= right:  # traversal complete, & one element is sorted when left == right
        return

    mid = (left + right) // 2
    merge_sort(A, left, mid)
    merge_sort(A, mid + 1, right)
    modified_merge_logic(A, left, mid, right)


def rearrange_via_modified_merge_sort(A):
    merge_sort(A, left=0, right=len(A) - 1)


if __name__ == "__main__":
    arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
    # arr = [12, 11, -13, -5, 6, -7, 5, -3, -6]
    rearrange_via_modified_merge_sort(arr)
    print(arr)

"""
[12,11,-13,-5,6,-7,5,-3,-6]
[-1, 2, -3, 4, 5, 6, -7, 8, 9]
[2, 3, -1, -4, -6]                          # Reverse
[4, 3, 2, 1, 0, -1, -2, -3]                 # Reverse containing 0
"""
