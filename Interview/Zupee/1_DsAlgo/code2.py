# You have given an array of non-negative integers.
# Each element in the array represents your maximum jump length at that position,
# you are initially positioned at the first index of the array.
# Return the minimum number of jumps required to reach the last index.
# If it is not possible to reach the last index, return -1.

"""
Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
Output: 3 (1-> 3 -> 8 -> 9)
Explanation: Jump from 1st element
to 2nd element as there is only 1 step,
now there are three options 5, 8 or 9.
If 8 or 9 is chosen then the end node 9
can be reached. So 3 jumps are made.

Input:  arr[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
Output: 10
Explanation: In every step a jump
is needed so the count of jumps is 10.
"""

# [1, 3]
# Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}


def find_min_jumps(arr, curr=0) -> int:
    options = arr[curr]  # value in the array

    min_jump = ?
    for i in range(options):
        no_of_jumps = find_min_jumps(arr, (curr + i + 1))
        min_jump = min(no_of_jumps, min_jump)

    min_jump