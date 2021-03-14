from Utils.Array import input_array


# Not Inplace
def prefix_sum(actual_array) -> list:
    n = len(actual_array)

    arr = [num for num in actual_array]  # making a copy of actual_array    # Notice : only change

    for i in range(1, n):  # From 1 to n-1
        arr[i] = arr[i] + arr[i - 1]

    return arr


if __name__ == '__main__':
    array = input_array()
    prefix_sum_arr = prefix_sum(array)
    print(prefix_sum_arr)

"""
6 3 -2 4 -1 0 -5
"""
