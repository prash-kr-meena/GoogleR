from Utils.Array import input_array

"""
1 0 0 0 1 0 1          4 0's    3 1's

0 1 0 1

largest sub_array with all equal 0's and 1's
contiguous subarray


brute force : O(n2)
Optimization



3 2 2 2 2 1 1
1 0 0 0 1 0 1 <<<<
1 1 1 1 2 2 3


-2 -3 -2  0  1  0  1
1 -1  -1 -1  1 -1  1 <<<<
1  0  -1 -2 -1 -2 -1




 1  1  0  0   1  1  0  0  ^  0  0  0
 1  1 -1  -1  1  1 -1  -1 ^ -1  -1  -1        <<<<<<<<<
 1  2  1  0   1  2  1   0  ^ -1 -2 -3


  0   0   0   0   1   0   0   0  ^   0   0   0
 -1  -1  -1  -1   1  -1  -1  -1  ^  -1  -1  -1  <<<<<<<
 -1 - 2  -3  -4   -3 -4  -5  -6     -7  -8  -9



store : 1 : 3   -> 2
        0 : 4   -> 2


1 0 0 0 1 0 1
L           R

1 0 0 0 1 0 1
      L     R

1 0 0 0 1 0 1
L  R
"""


def find_largest_subarray_with_equal_0_nd_1(arr):
    n = len(arr)  # or brr
    brr = []
    for e in arr:
        if e == 0:
            brr.append(-1)
        else:
            brr.append(e)

    # prefix sum
    for i in range(1, n):
        brr[i] = brr[i] + brr[i - 1]

    # dictionary of value -> idx
    largest_subarray_length = 0
    left = None
    right = None

    mapping = {}
    for idx, val in enumerate(brr):
        if val in mapping:
            length = idx - (mapping.get(val) + 1)
            if length >= largest_subarray_length:
                largest_subarray_length = length + 1
                left = mapping.get(val) + 1
                right = idx

            mapping[val] = idx  # update the indexing
        else:
            mapping[val] = idx

    print(mapping)
    print(largest_subarray_length, left, right)
    print(brr)


#  1  1  0  0  1  1  0  0   0  0  0
# [1, 2, 1, 0, 1, 2, 1, 0, -1, -2, -3]

if __name__ == '__main__':
    array = input_array()
    find_largest_subarray_with_equal_0_nd_1(array)
"""
1  1  0  0   1  1  0  0   0  0  0
"""
