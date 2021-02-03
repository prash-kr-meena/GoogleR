def solve_knapsack(profits, weights, capacity):
    # basic checks
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp = [0 for x in range(capacity + 1)]  # <<<<<<<<<<

    # if we have only one weight, we will take it if it is not more than the capacity
    for c in range(0, capacity + 1):
        if weights[0] <= c:
            dp[c] = profits[0]

    # process all sub-arrays for all the capacities
    for i in range(1, n):
        for c in range(capacity, -1, -1):  # <<<<<<<<
            profit_by_including, profit_by_excluding = 0, 0

            if weights[i] <= c:  # include the item, if it is not more than the capacity
                profit_by_including = profits[i] + dp[c - weights[i]]

            profit_by_excluding = dp[c]  # exclude the item

            dp[c] = max(profit_by_including, profit_by_excluding)  # take maximum

    return dp[capacity]


if __name__ == '__main__':
    print("Total knapsack profit: ", str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7)))
    print("Total knapsack profit: ", str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6)))
