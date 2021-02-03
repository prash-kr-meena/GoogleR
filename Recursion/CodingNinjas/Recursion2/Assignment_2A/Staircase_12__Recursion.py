from sys import setrecursionlimit

# https://leetcode.com/problems/climbing-stairs/
# Implementation, for the problem where the user can take 0 or 1 step

"""
Note : the Code is correct, but it will not be accepted over Leet-Code,
       as it expects it to be solved using dynamic programming

       But to verify your solution, you can go in the testcase tab, and put values like 20
       which after running, you can verify with their expected result
"""


def ways(n) -> int:
    if n == 1 or n == 2:
        return n

    return ways(n - 1) + ways(n - 2)


if __name__ == '__main__':
    setrecursionlimit(11000)
    staircases = int(input())  # no of stairs
    print(ways(staircases))
