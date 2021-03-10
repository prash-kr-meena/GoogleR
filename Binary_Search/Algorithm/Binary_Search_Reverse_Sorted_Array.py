from Utils.Array import input_array


# Exactly Similar : Just reversing the logic of finding element
def binary_search_reverse_sorted_array(reverse_sorted_array, key) -> int:
    left = 0
    right = len(reverse_sorted_array) - 1

    while left <= right:
        mid = (left + right) // 2
        if reverse_sorted_array[mid] > key:  # go right
            left = mid + 1
        elif reverse_sorted_array[mid] < key:  # go left
            right = mid - 1
        else:  # found it
            return mid

    return -1


if __name__ == "__main__":
    array = input_array()
    search_key = int(input())
    index = binary_search_reverse_sorted_array(array, search_key)

    print("{} \nKey : {} \nIndex : {}".format(array, search_key, index))

"""
 9 8 7 6 5 4 3 2 1
 6

# 2 as duplicates   -   Index Not Guaranteed
5 4 2 2 2 1
2

# 2 as duplicates   -   Index Not Guaranteed
10 9 8 7 6 5 4 2 2 2 1
2
"""
