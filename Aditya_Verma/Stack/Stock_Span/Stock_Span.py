from Aditya_Verma.Stack.Index__Greater_n_Smaller_Nums_To_Left_n_Right.NGL_Index import \
    indexes_of_next_greater_element_to_left


# You can remove the first two if's, that will work too
# Optimized stack solution
# O(n) Time
# O(n) Space
def get_result_array(ngl_index_array):
    length = len(ngl_index_array)
    res = [-1] * length

    for i in range(0, length):
        res[i] = i - ngl_index_array[i]

    return res


if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    ngl_index_array = indexes_of_next_greater_element_to_left(arr)
    print(get_result_array(ngl_index_array))

"""
10 5 11 10 20 12
100 80 60 70 60 75 85
"""
