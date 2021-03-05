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
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # we don't want to delete any interval from the list, as it will cause extra time of O(n)
        # instead we can have a boolean array specifying if we have processed it, when we found that it overlaps

        rows = len(intervals)
        columns = len(intervals[0])

        already_merged = [False] * rows

        for i in range(rows):
            if already_merged[i] is True:  # notice
                continue

            for j in range(rows):  # for each i (0 to N), go through all j (0 to N), only skipp where i==j

                if i == j:  # same interval, will always overlap, don't process them
                    continue
                if already_merged[j] is True:  # notice
                    continue

                ith_interval = intervals[i]
                jth_interval = intervals[j]
                if is_overlapping(ith_interval, jth_interval):
                    # update my ith_interval and mark jth_interval as merged
                    already_merged[j] = True
                    ith_interval[0] = min(ith_interval[0], jth_interval[0])  # minimum starting
                    ith_interval[1] = max(ith_interval[1], jth_interval[1])  # maximum ending

        result = []
        for idx, interval in enumerate(intervals):
            if already_merged[idx] is False:
                result.append(interval)

        return result


if __name__ == '__main__':
    interval_matrix = input_integer_matrix()
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

# Note : Why brute force is not working
"""
Why this brute force approach will not work : Even though it might look it will pass all the test case
WELL to be honest this will pass most cases, but there is a particular scenario when this will fail and will be hard to reason about


My Approach : 
I pick one interval, `interval[i]`
and then for that interval I check all the other intervals `interval[j]` from start to end
==> so even if i am at an interval i=3 say, 
    i will still compare with all the intervals from j=0 to j=size-1
    except when j==i, ill skipp that because that will obviously overlap, as both intervals are same


now when I am processing interval-i, and for that i am going to all the intervals-j
when i find a match, of interval-i and interval-j
What i am doing is i am 
    1. Updating my interval-i's values, each time I find an overlap
    2. marking my interval-j as processed

 AND this is where i am making a mistake, due to which my test cases are failing
 
 
 

[[3,5],[0,0],[4,4],[0,2],[5,6],[4,5],[3,5],[1,3],[4,6],[4,6],[3,4]]
[  F  ,  F  ,  F  ,  F  ,  F  ,  F  ,  F  ,  F  ,  F  ,  F  ,  F  ]       <<<<<<<<, All False Initially

process [3,5]  --> and it turns into [1,6]
[FALSE,FALSE,  T  ,FALSE,  T  ,  T  ,  T  ,  T  ,  T  ,  T  ,  T  ]      << all except interval [0,0] & [0,2] matches

Noe Processing [0,0]  --> [0,2]
[FALSE,FALSE,  T  ,__T__,  T  ,  T  ,  T  ,  T  ,  T  ,  T  ,  T  ]      << interval [0,2] overlaps


now if you see, after the [0,0] interval, all the intervals are marked to be processed, so the iteration stops
and we have the updated intervals
[1,6] and [0,2]


But if you see this is wrong, because they are still overlapping and form an interval [0,6]


and this is happening because of the reason mentioned above, 
so instead
if we do the opposite, ie 
    1. Updating my interval-J's values, each time I find an overlap
    2. marking my interval-I as processed
    
and this is what we have don in the correct brute force solution 
"""
