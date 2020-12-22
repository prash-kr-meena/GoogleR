def solve_knapsack(profits, weights, capacity):
    # basic checks
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp = [[0 for x in range(capacity + 1)] for y in range(n)]

    # populate the capacity = 0 columns, with '0' capacity we have '0' profit   # Note : we already have 0's
    for i in range(0, n):  # i is row_index
        dp[i][0] = 0

    # if we have only one weight, we will take it if it is not more than the capacity
    for c in range(0, capacity + 1):  # c is capacity & column_index
        if weights[0] <= c:
            dp[0][c] = profits[0]

    # process all sub-arrays for all the capacities
    for i in range(1, n):
        for c in range(1, capacity + 1):
            profit_by_including, profit_by_excluding = 0, 0

            if weights[i] <= c:  # include the item, if it is not more than the capacity
                profit_by_including = profits[i] + dp[i - 1][c - weights[i]]

            profit_by_excluding = dp[i - 1][c]  # exclude the item

            dp[i][c] = max(profit_by_including, profit_by_excluding)  # take maximum

    return dp[n - 1][capacity]  # maximum profit will be at the bottom-right corner


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
