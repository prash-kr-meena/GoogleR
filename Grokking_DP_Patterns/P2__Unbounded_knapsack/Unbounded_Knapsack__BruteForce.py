def solve_knapsack(profits, weights, capacity):
    if profits is None \
            or weights is None \
            or len(profits) == 0 \
            or len(profits) != len(weights):
        return 0

    return unbounded_knapsack(profits, weights, capacity, 0)


# We are trying to find the maximum profit
def unbounded_knapsack(profits, weights, capacity, curr_index):
    n = len(profits)  # or len(weights)
    if capacity <= 0 or curr_index >= n:  # base checks
        return 0

    # recursive call after choosing the items at the curr_index,
    # Note that we recursive call on all items as we did not increment curr_index
    profit_by_inclusion = 0
    if weights[curr_index] <= capacity:
        profit_by_inclusion = profits[curr_index] + \
                              unbounded_knapsack(profits, weights, capacity - weights[curr_index], curr_index)

    # recursive call after excluding the element at the currentIndex
    profit_by_exclusion = unbounded_knapsack(profits, weights, capacity, curr_index + 1)

    return max(profit_by_inclusion, profit_by_exclusion)


def main():
    print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 8))
    print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 6))


main()
