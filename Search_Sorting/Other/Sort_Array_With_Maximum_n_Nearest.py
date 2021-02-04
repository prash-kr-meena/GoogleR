from Utils.Array import input_array


def sort_array_with_maximum_n_nearest(arr):
    n = len(arr)  # Notice

    # getting a mapping of the value and the index
    tupl_arr = [(idx, val) for idx, val in enumerate(arr)]
    print(tupl_arr)

    # First sort on the value, Max-Value should come first
    # But if the values are similar, then the closer value should come first
    sorted_tpl_arr = sorted(tupl_arr, key=lambda e: (e[1], n - e[0]), reverse=True)  # Notice : use of n
    print(sorted_tpl_arr)


if __name__ == '__main__':
    array = input_array()
    sort_array_with_maximum_n_nearest(array)

"""
1 1 2 3 3 4 1 2


1' 1" 2' 3' 3" 4  2"        Input
4  3' 3" 2' 2" 1' 1"        Output
"""
