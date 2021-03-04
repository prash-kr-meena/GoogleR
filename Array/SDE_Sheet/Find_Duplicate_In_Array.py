from typing import List

from Utils.Array import input_array

"""
Find the duplicate in an array of N integers

Arrays Google Doc   : https://docs.google.com/document/d/1NUoBX8WzYYkKRQdIxuN_K_406NtmBm5vfL0AzEceaHQ/edit#heading=h.84llj8puqlhz
LeetCode            : https://leetcode.com/problems/find-the-duplicate-number/
"""

"""
Read through the google document, to get more understanding

Implementing the most optimized solution
Floyds Cycle Detection algorithm, and Finding the cycle intersection

Accepted on leetcode
"""

"""
This algorithm works, when the constraints are that
we can't user extra storage, and we also can't change the array (ie sorting will not be allowed)

alternate approaches exist, like by having a hashmap to store frequency 
or 
by sorting the array
But when these two approaches are not acceptable then we need to use this Floyds algorithm 
"""


class Solution:
    def find_duplicate(self, arr: List[int]) -> int:
        # edge case : the array has to be of size, more then or equal to 2
        if arr is None or len(arr) <= 1:
            return -1

        # will start from the 0th index
        slow = arr[0]
        fast = arr[0]

        while True:  # Infinite loop, as it is guaranteed that there will be cycle
            slow = arr[slow]
            fast = arr[arr[fast]]  # two hops
            if slow == fast:
                break

        # cycle detected, now find the intersection point (cycles starting point)
        # slow, starts from arr[0] and, fast now walks like slow ie one hop each time
        slow = arr[0]
        while slow != fast:
            slow = arr[slow]
            fast = arr[fast]  # only one hop

        return slow  # or fast


if __name__ == '__main__':
    array = input_array()
    print(Solution().find_duplicate(array))

"""
1 3 4 2 2
3 3 3 3 2
2 5 9 6 9 3 8 9 7 1         // With a cycle
1 2 3 4 5 6 7               // Without cycle ArrayIndexOutOfBoundsException
"""
