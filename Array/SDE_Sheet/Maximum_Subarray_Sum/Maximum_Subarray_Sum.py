from Utils.Array import input_array

"""
Kadance Algorithm

Submitted on Leetcode : https://leetcode.com/problems/maximum-subarray/
Striver : https://www.youtube.com/watch?v=w_KEocd__20&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=9&ab_channel=takeUforward

NOTE : the elements also contains -ve elements as well

Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.
"""


def maximum_sub_array_sum_brute_force(A) -> int:
    """
    basically going through all the sub-arrays and finding there sum, and maintaining the max
    Time  : O(n^2)          You can do it in O(n^3) as well
    Space : O(1)
    """
    n = len(A)
    max_sum = float("-inf")

    for i in range(n):
        sub_array_sum = 0
        for j in range(i, n):
            sub_array_sum += A[j]
            max_sum = max(max_sum, sub_array_sum)

    return max_sum


def maximum_sub_array_sum__kadance(A) -> (int, int, int):
    """
    Time  : O(n)
    Space : O(1)
    """
    n = len(A)

    start = end = 0  # sub-array start and end                              # EXTRA notice
    s = 0  # auxiliary variable, to update correct location of start        # EXTRA notice

    curr_sum = 0  # That will follow through
    max_sum = A[0]  # To maintain max_sum, A[0] initially because we need at-least one element, so lets choose A[0]

    for i in range(0, n):
        curr_sum += A[i]

        if curr_sum > max_sum:  # writing it earlier is Important
            max_sum = curr_sum  # as before updating the max_sum you can't update curr_sum to 0, even if its less then 0
            start = s  # EXTRA notice
            end = i  # EXTRA notice

        if curr_sum < 0:  # As any sub_array with -ve sum will not conclude into our answer
            curr_sum = 0
            s = i + 1  # EXTRA notice

    return max_sum, start, end


if __name__ == '__main__':
    array = input_array()
    print(maximum_sub_array_sum_brute_force(array))
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


Input : -2 -3 4 -1 -2 1 5 -3             When all the numbers are -ve
Output: 7
"""
