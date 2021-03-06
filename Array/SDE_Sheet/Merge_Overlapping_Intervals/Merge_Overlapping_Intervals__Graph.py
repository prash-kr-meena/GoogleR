from typing import List
from Utils.Matrix import input_integer_matrix

"""
Merge Overlapping Sub-Intervals
Google Doc : https://docs.google.com/document/d/1NUoBX8WzYYkKRQdIxuN_K_406NtmBm5vfL0AzEceaHQ/edit#heading=h.sbfmvevouadr
Leet-Code : https://leetcode.com/problems/merge-intervals/
"""

"""
The Graph implementation will also not be optimal
as it will also be O(n2) only

We can do this in graphs using the concept of Connected Components
"""


# TODO


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        pass


if __name__ == '__main__':
    interval_matrix = input_integer_matrix()
    print(interval_matrix)
    pass

"""
[[1,3],[2,6],[8,10],[15,18]]

4
1 3
2 6
8 10
15 18
"""
