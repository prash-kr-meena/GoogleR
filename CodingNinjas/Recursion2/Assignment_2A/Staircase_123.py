from sys import setrecursionlimit

"""
Give, he can hop 1 step, 2 step, or 3 step at a time
1 <= N <= 30      at least one step is there


Time : O(3^n) exponential
"""


def ways_to_reach(stairs) -> int:
    # Base Case -> not particular to this question, as here it is given the N >= 1
    if stairs == 0:
        return 0  # 0 ways to reach

    # Base Case
    if stairs == 1:
        return 1  # One possible way
    elif stairs == 2:
        return 2
    elif stairs == 3:  # as we have included stairs == 0 base case, we can exclude it
        return 4

    # Hypothesis

    total_ways_to_reach___n_minus_1_stairs = ways_to_reach(stairs - 1)
    total_ways_to_reach___n_minus_2_stairs = ways_to_reach(stairs - 2)
    total_ways_to_reach___n_minus_3_stairs = ways_to_reach(stairs - 3)

    # Induction
    return total_ways_to_reach___n_minus_1_stairs \
           + total_ways_to_reach___n_minus_2_stairs \
           + total_ways_to_reach___n_minus_3_stairs


if __name__ == '__main__':
    setrecursionlimit(11000)
    staircases = int(input())  # no of stairs
    print(ways_to_reach(staircases))
