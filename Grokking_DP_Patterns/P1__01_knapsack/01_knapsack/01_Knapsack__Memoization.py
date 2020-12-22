def solve_knapsack(profits, weights, capacity):
    # Create a two dimensional array for Memoization, each element is initialized to '-1'
    dp = [[-1 for x in range(capacity + 1)] for y in range(len(profits))]  # use profits or weights, both same size
    return knapsack_recursive(dp, profits, weights, capacity, 0)


def knapsack_recursive(dp, profits, weights, capacity, current_index):
    # base checks
    if capacity <= 0 or current_index >= len(profits):  # or weights
        return 0

    # if we have already solved a similar problem, return the result from memory
    if dp[current_index][capacity] != -1:
        return dp[current_index][capacity]

    # recursive call after choosing the element at the currentIndex
    # if the weight of the element at currentIndex exceeds the capacity, we shouldn't process this
    profit_by_including = 0
    if weights[current_index] <= capacity:
        profit_by_including = profits[current_index] + knapsack_recursive(dp, profits, weights,
                                                                          capacity - weights[current_index],
                                                                          current_index + 1)

    # recursive call after excluding the element at the currentIndex
    profit_by_excluding = knapsack_recursive(dp, profits, weights, capacity, current_index + 1)

    dp[current_index][capacity] = max(profit_by_including, profit_by_excluding)
    return dp[current_index][capacity]


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
