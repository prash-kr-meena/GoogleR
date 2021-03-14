from Utils.Array import input_array

"""
Kadance _Algorithm
GeeksForGeeks : https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
"""


def maximum_sub_array_sum__kadance(A) -> int:
    n = len(A)

    curr_sum = 0  # That will follow through
    max_sum = A[0]  # To maintain max_sum, A[0] initially because we need at-least one element, so lets choose A[0]

    for i in range(0, n):
        curr_sum += A[i]

        if curr_sum > max_sum:  # writing it earlier is Important: notice
            max_sum = curr_sum  # as before updating the max_sum you can't update curr_sum to 0, even if its less then 0

        if curr_sum < 0:  # As any sub_array with -ve sum will not conclude into our answer
            curr_sum = 0

    return max_sum


if __name__ == '__main__':
    array = input_array()
    print(maximum_sub_array_sum__kadance(array))

"""
Input : -2 1 -3 4 -1 2 1 -5 4
Output: 6                               Explanation: [4 -1 2 1] has the largest sum = 6.

Input : 1
Output: 1

Input : 0
Output: 0

Input : 1 -1 2 4 -5 6 -8
Output: 7
"""
