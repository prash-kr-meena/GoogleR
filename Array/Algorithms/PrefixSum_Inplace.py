from Utils.Array import input_array


def prefix_sum_inplace(arr) -> None:
    n = len(arr)
    for i in range(1, n):  # From 1 to n-1
        arr[i] = arr[i] + arr[i - 1]


if __name__ == '__main__':
    array = input_array()
    prefix_sum_inplace(array)
    print(array)

"""
6 3 -2 4 -1 0 -5
"""
