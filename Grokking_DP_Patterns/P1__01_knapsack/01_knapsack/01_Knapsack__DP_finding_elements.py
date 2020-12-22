def solve_knapsack(profits, weights, capacity):
    # basic checks
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp = [[0 for x in range(capacity + 1)] for y in range(n)]

    # populate the capacity = 0 columns, with '0' capacity we have '0' profit
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

    print_selected_elements(dp, weights, profits, capacity)  # <<<<<<<<
    return dp[n - 1][capacity]  # maximum profit will be at the bottom-right corner


def print_selected_elements(dp, weights, profits, capacity):
    print("Selected weights are: ", end='')  # instead you could have a list of elements that you could print at last

    n = len(weights)
    total_profit = dp[n - 1][capacity]

    for i in range(n - 1, 0, -1):  # 0 is not inclusive, ie [n-1, 0)
        if total_profit != dp[i - 1][capacity]:
            print(str(weights[i]) + " ", end='')
            capacity -= weights[i]
            total_profit -= profits[i]

    if total_profit != 0:
        print(str(weights[0]) + " ", end='')


def main():
    print("\nTotal knapsack profit: ", str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7)))
    print("\nTotal knapsack profit: ", str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6)))


main()
