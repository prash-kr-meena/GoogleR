# max = float("-inf")
from sys import setrecursionlimit


def can_include_this_job(job, included_jobs):
    print("included", included_jobs)
    for curr_job in included_jobs:
        if not (job[0] >= curr_job[1] or job[1] <= curr_job[0]):
            return False
    return True


def find_max_profit(jobs, curr, included_jobs) -> int:
    if curr > len(jobs) - 1:
        return 0

    print(included_jobs, "<")
    max_profit_if_including = 0
    if can_include_this_job(jobs[i], included_jobs):
        included_jobs.append(jobs[i])
        max_profit_if_including = find_max_profit(jobs, i + 1, included_jobs) + jobs[i][2]
        included_jobs.pop()

    max_profit_if_excluding = find_max_profit(jobs, i + 1, included_jobs)

    max_profit = max(max_profit_if_including, max_profit_if_excluding)
    return max_profit


if __name__ == '__main__':
    setrecursionlimit(11000)
    n = int(input())
    jobs = []
    for i in range(n):
        start, end, profit = map(int, input().strip().split())
        jobs.append((start, end, profit))
    max_profit = find_max_profit(jobs, 0, [])
    print(max_profit)

"""

2
1 2 100
2 3 200

INPUT
4
1 2 100
2 3 200
3 5 300
2 7 700

Job1: {start: 1, end: 2, profit: 100}
Job2: {start: 2, end: 3, profit: 200}
Job3: {start: 3, end: 5, profit: 300}
Job4: {start: 2, end: 7, profit: 700}

Max Profit: 800
NOTE : matching values don't consider them overlapping


Find the maximum profit out the given jobs
The jobs are required to not have overlapping overlapping of jobs.

Optimize overlappoing
Optimize the O(exponential) appocah using Memoization



1 2 3 4

1 2  = 300
1 = 100

1 2 3 = 600
1 3= 400


"""
