def count_subsetsum(nums, sum) -> int:
    n = len(nums)
    row_size = n + 1
    col_size = sum + 1
    dp = [[-1 for x in range(col_size)] for y in range(row_size)]

    # Base Case -> Initialization
    for j in range(1, col_size):  # Filling 0th row by 0, leaving dp[0][0]
        dp[0][j] = 0

    for i in range(row_size):  # Filling 0th col by 1 (including dp[0][0] )
        dp[i][0] = 1

    # Coding the choice diagram
    # DO NOT override the initialization values, NOTE
    for i in range(1, row_size):
        for j in range(1, col_size):
            if nums[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - nums[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][sum]


if __name__ == "__main__":
    print(count_subsetsum([1, 2, 3, 3], 6))
    print(count_subsetsum([1, 1, 1, 1], 1))
