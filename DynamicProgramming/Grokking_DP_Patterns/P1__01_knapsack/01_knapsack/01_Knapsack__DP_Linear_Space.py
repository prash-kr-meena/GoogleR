def solve_knapsack(profits, weights, capacity):
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:  # basic checks
        return 0

    # We only need one previous row to find the optimal solution,
    # Overall we need '2' rows, the solution is similar to the previous solution, the only difference is that
    # we use `i % 2` instead if `i` and `(i-1) % 2` instead if `i-1`      when querying the DP matrix
    dp = [[0 for x in range(capacity + 1)] for y in range(2)]

    # if we have only one weight, we will take it if it is not more than the capacity
    for c in range(0, capacity + 1):
        if weights[0] <= c:
            dp[0][c] = dp[1][c] = profits[0]  # Note : Updating data in both the rows **

    # process all sub-arrays for all the capacities
    for i in range(1, n):
        for c in range(0, capacity + 1):
            profit_by_including, profit_by_excluding = 0, 0

            if weights[i] <= c:  # include the item, if it is not more than the capacity
                profit_by_including = profits[i] + dp[(i - 1) % 2][c - weights[i]]

            profit_by_excluding = dp[(i - 1) % 2][c]  # exclude the item

            dp[i % 2][c] = max(profit_by_including, profit_by_excluding)  # take maximum

    return dp[(n - 1) % 2][capacity]


if __name__ == '__main__':
    print("Total knapsack profit: ", str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7)))
    print("Total knapsack profit: ", str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6)))
