from typing import List
from Utils.Matrix import input_matrix

"""
Merge Overlapping Subintervals
Google Doc : https://docs.google.com/document/d/1NUoBX8WzYYkKRQdIxuN_K_406NtmBm5vfL0AzEceaHQ/edit#heading=h.sbfmvevouadr
Submitted on LeetCode : https://leetcode.com/problems/merge-intervals/
"""

"""
Implementing the optimized solution via sorting
Now the idea is if the intervals are sorted in the order of the start_time
then we know that, the intervals that can be overlapped will be adjacent to each other

hence, we would not need to two an n2 approach, 
and we could just to it in one pass, ie O(n) only

But note that sorting will take O(n log n) time 
"""


def is_overlapping(interval_i, interval_j) -> bool:
    return not (interval_i[0] > interval_j[1] or interval_i[1] < interval_j[0])


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()  # by default it will sort on the first element of the pair only

        processed = [False] * n

        for i in range(1, n):
            curr_interval = intervals[i]
            prev_interval = intervals[i - 1]
            if is_overlapping(curr_interval, prev_interval):
                # mark  the prev_interval (i-1 th) as processed and update the curr_interval (ith)
                processed[i - 1] = True
                curr_interval[0] = min(curr_interval[0], prev_interval[0])
                curr_interval[1] = max(curr_interval[1], prev_interval[1])

        result = [interval for idx, interval in enumerate(intervals) if processed[idx] is False]
        return result


if __name__ == '__main__':
    interval_matrix = input_matrix("")
    print(Solution().merge(interval_matrix))

"""
[[1,3],[2,6],[8,10],[15,18]]

4
1 3
2 6
8 10
15 18
"""

"""
[[3,5],[0,0],[4,4],[0,2],[5,6],[4,5],[3,5],[1,3],[4,6],[4,6],[3,4]]       GOOD TEST CASE       Brute Force Fails here
11
3 5
0 0
4 4
0 2
5 6
4 5
3 5
1 3
4 6
4 6
3 4
"""
