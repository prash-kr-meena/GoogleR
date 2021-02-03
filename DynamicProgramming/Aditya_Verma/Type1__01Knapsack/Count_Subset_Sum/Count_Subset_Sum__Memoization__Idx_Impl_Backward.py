# Recursion1 using input-output method
# The choice diagram is same as of 01 knapsack
from Utils.Matrix import get_filled_matrix


def count_subsetsum(nums, sum, n, dp) -> int:
    # Base Case
    if n == 0 and sum != 0:
        return 0  # can't form any subset

    if sum == 0:  # empty subset, regardless of n==0 or n!=0
        return 1

    if dp[n][sum] != -1:  # MEMOIZE
        return dp[n][sum]

    # Choice Diagram
    if nums[n - 1] <= sum:  # Two choices
        subset_sum_count__when_including_curr_num = count_subsetsum(nums, sum - nums[n - 1], n - 1, dp)
        subset_sum_count__when_NOT_including_curr_num = count_subsetsum(nums, sum, n - 1, dp)
        dp[n][sum] = subset_sum_count__when_including_curr_num + subset_sum_count__when_NOT_including_curr_num
        return dp[n][sum]
    else:  # Once Choice
        dp[n][sum] = count_subsetsum(nums, sum, n - 1, dp)  # subset_sum_count__when_NOT_including_curr_num
        return dp[n][sum]


def solve_subsetsum_count(nums, sum):
    n = len(nums)
    dp = get_filled_matrix(row_size=n + 1, col_size=sum + 1, fill=-1)
    return count_subsetsum(nums, sum, n, dp)


if __name__ == "__main__":
    print(solve_subsetsum_count([1, 2, 3, 3], 6))
    print(solve_subsetsum_count([1, 1, 1, 1], 1))
