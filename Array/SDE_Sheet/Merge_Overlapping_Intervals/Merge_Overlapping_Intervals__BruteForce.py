from typing import List
from Utils.Matrix import input_integer_matrix

"""
Merge Overlapping Subintervals
Google Doc : https://docs.google.com/document/d/1NUoBX8WzYYkKRQdIxuN_K_406NtmBm5vfL0AzEceaHQ/edit#heading=h.sbfmvevouadr
Leet Code : https://leetcode.com/problems/merge-intervals/
"""

"""
Implementing the Brute Force Solution
of comparing all the intervals with each other 
"""


def do_overlap(interval_i, interval_j) -> bool:
    return not (interval_i[0] > interval_j[1] or interval_i[1] < interval_j[0])


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # we don't want to delete any interval from the list, as it will cause extra time of O(n)
        # instead we can have a boolean array specifying if we have processed it, when we found that it overlaps

        rows = len(intervals)
        columns = len(intervals[0])

        already_merged = [False] * rows

        for i in range(rows):
            for j in range(rows):
                if i == j:  # same interval, will always overlap, don't process them
                    continue
                if already_merged[j] is True:
                    continue

                ith_interval = intervals[i]
                jth_interval = intervals[j]
                if do_overlap(ith_interval, jth_interval):
                    # update my ith_interval and mark jth_interval as merged
                    already_merged[j] = True
                    ith_interval[0] = min(ith_interval[0], jth_interval[0])  # minimum starting
                    ith_interval[1] = max(ith_interval[1], jth_interval[1])  # maximum ending

            # already_merged[i] = True  # we have processed ith interval

        print(intervals)
        print(already_merged)
        for idx, interval in enumerate(intervals):
            if already_merged[idx] is False:
                print(interval)


# Note: Not Correct right now --> correct now

if __name__ == '__main__':
    interval_matrix = input_integer_matrix()
    Solution().merge(interval_matrix)

"""
[[1,3],[2,6],[8,10],[15,18]]

4
1 3
2 6
8 10
15 18
"""
