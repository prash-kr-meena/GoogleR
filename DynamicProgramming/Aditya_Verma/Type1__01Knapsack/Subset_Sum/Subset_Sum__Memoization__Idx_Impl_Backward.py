# Recursion1 using input-output method
# The choice diagram is same as of 01 knapsack
from Utils.Matrix import get_filled_matrix


def subsetsum(nums, sum, n, dp) -> bool:
    # Base Case
    if n == 0 and sum > 0:
        return False
    if sum == 0:
        return True

    if dp[n][sum] is not None:  # Memoization
        return dp[n][sum]

    if nums[n - 1] <= sum:
        dp[n][sum] = subsetsum(nums, sum - nums[n - 1], n - 1, dp) or subsetsum(nums, sum, n - 1, dp)
        return dp[n][sum]  # Memoization
    else:
        dp[n][sum] = subsetsum(nums, sum, n - 1, dp)
        return dp[n][sum]  # Memoization


def solve_subsetsum(nums, sum) -> bool:
    n = len(nums)
    dp = get_filled_matrix(row_size=n + 1, col_size=sum + 1, fill=None)
    result = subsetsum(nums, sum, n, dp)
    return result


if __name__ == "__main__":
    print(solve_subsetsum([3, 34, 4, 12, 5, 2], 9))
    print(solve_subsetsum([3, 34, 4, 12, 5, 2], 30))
