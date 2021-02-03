def solve_knapsack(profits, weights, capacity):
    return knapsack_recursive(profits, weights, capacity, 0)


def knapsack_recursive(profits, weights, capacity, current_index):
    # base checks
    if capacity <= 0 or current_index >= len(profits):
        return 0

    # recursive call after choosing the element at the currentIndex
    # if the weight of the element at currentIndex exceeds the capacity, we  shouldn't process this
    profit_by_excluding = 0
    if weights[current_index] <= capacity:
        profit_by_excluding = profits[current_index] + knapsack_recursive(profits, weights,
                                                                          capacity - weights[current_index],
                                                                          current_index + 1)

    # recursive call after excluding the element at the currentIndex
    profit_by_including = knapsack_recursive(profits, weights, capacity, current_index + 1)

    return max(profit_by_excluding, profit_by_including)


if __name__ == '__main__':
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))

# output
# 22
# 17
