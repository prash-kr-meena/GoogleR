"""
Given a sequence of n unique sorted integers and a number k,
find the k'th missing integer in the sequence starting from the left most number in the sequence.

1 2 3 4 5  6* 7 8* 9

k = 1
6

k = 2
8

k =3
10


4 5 6 7 8
k = 1  => 9   not 1
k = 5

k >= 1   Constraint


4 5 6* 7 8


1-100
k = 1  => 2



Brute Force will be O(n+k)

optimized it to O(log n) using binary search
"""
from Utils.Array import input_array


def find_kth_missing_num(arr, k):
    n = len(arr) - 1
    left = 0
    right = n

    first_element = arr[0]

    while left < right:
        mid = (left + right) // 2
        mid_value = arr[mid]
        expected_value_at_mid = first_element + mid

        if mid_value == expected_value_at_mid:
            # go right - on left no number is missing
            left = mid + 1
        elif mid_value > expected_value_at_mid:
            no_of_missing_values = mid_value - expected_value_at_mid
            # to go left or right, it depend of on      {no_of_missing_values & k}

            if k > no_of_missing_values:
                # go to right, but also update the k
                left = mid + 1
                k = k - no_of_missing_values
            else:
                # go to left, but also update the k
                right = mid - 1
        else:
            print("mid_value < expected_value_at_mid  should not happen ")


if __name__ == '__main__':
    k = int(input())
    array = input_array()
    find_kth_missing_num(array, k)
