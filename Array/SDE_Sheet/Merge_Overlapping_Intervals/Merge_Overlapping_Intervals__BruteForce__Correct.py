from typing import List
from Utils.Matrix import input_integer_matrix

"""
Merge Overlapping Sub-Intervals
Google Doc : https://docs.google.com/document/d/1NUoBX8WzYYkKRQdIxuN_K_406NtmBm5vfL0AzEceaHQ/edit#heading=h.sbfmvevouadr
Leet Code : https://leetcode.com/problems/merge-intervals/
"""

"""
Implementing the Brute Force Solution
of comparing all the intervals with each other
"""


def is_overlapping(interval_i, interval_j) -> bool:
    return not (interval_i[0] > interval_j[1] or interval_i[1] < interval_j[0])


class Solution:
    # we don't want to delete any interval from the list, as it will cause extra time of O(n)
    # instead we can have a boolean array specifying if we have processed it, when we found that it overlaps

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        rows = len(intervals)
        processed = [False] * rows

        for i in range(0, rows - 1):
            for j in range(i + 1, rows):
                ith_interval = intervals[i]
                jth_interval = intervals[j]

                if is_overlapping(ith_interval, jth_interval):
                    # update my Jth_interval and mark Ith_interval as merged
                    jth_interval[0] = min(jth_interval[0], ith_interval[0])  # minimum starting
                    jth_interval[1] = max(jth_interval[1], ith_interval[1])  # maximum ending
                    processed[i] = True
                    break  # break the loop, so that now we start processing the i+1 th interval NOTICE
                    # Notice : That we are updating the interval which is next to us
                    #  and not the one from which we start, we mark that just processed

        # only taking the intervals who are not marked processed
        result = [interval for idx, interval in enumerate(intervals) if not processed[idx]]
        return result


if __name__ == '__main__':
    interval_matrix = input_integer_matrix("")
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
