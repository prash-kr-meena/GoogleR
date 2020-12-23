# Recursion1 using input-output method
# The choice diagram is same as of 01 knapsack


def subset_sum(nums, sum) -> bool:
    n = len(nums)
    row_size = n + 1
    col_size = sum + 1
    dp = [[False for x in range(col_size)] for y in range(row_size)]

    # Base Case -> Initialization
    for j in range(1, col_size):  # Filling 0th row by F, leaving dp[0][0]
        dp[0][j] = False

    for i in range(row_size):  # Filling 0th col by T (including dp[0][0] )
        dp[i][0] = True

    # Coding the choice diagram
    # DO NOT override the initialization values, NOTE
    for i in range(1, row_size):
        for j in range(1, col_size):
            curr_num = nums[i - 1]  # as i is 1_indexed
            if curr_num <= j:
                dp[i][j] = dp[i - 1][j - curr_num] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][sum]


if __name__ == "__main__":
    print(subset_sum([3, 34, 4, 12, 5, 2], 4))
    print(subset_sum([3, 34, 4, 12, 5, 2], 1))
