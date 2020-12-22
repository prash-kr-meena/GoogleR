# Here, we are using index to traverse the array, But we are doing it in the reverse order
# Returns: an int denoting the maximum profit, that can be achieved
def max_profit_in_01knapsack(weight, value, capacity, n) -> int:
    # Base Case
    if n == 0 or capacity == 0:
        return 0  # Max Profit that can be generated with these inputs will be 0

    # choosing the current item from end of the list
    curr_item_wt = weight[n - 1]
    curr_item_val = value[n - 1]

    if curr_item_wt <= capacity:
        # We have option for choosing it and not choosing it
        profit_after_choosing_curr_item = curr_item_val + \
                                          max_profit_in_01knapsack(weight, value, capacity - curr_item_wt, n - 1)
        profit_after_NOT_choosing_curr_item = max_profit_in_01knapsack(weight, value, capacity, n - 1)
        return max(profit_after_choosing_curr_item, profit_after_NOT_choosing_curr_item)
    else:
        # We can't choose it
        profit_after_NOT_choosing_curr_item = max_profit_in_01knapsack(weight, value, capacity, n - 1)
        return profit_after_NOT_choosing_curr_item


def solve_01knapsack(weight, value, capacity):
    if len(weight) != len(value):
        raise ValueError("Invalid Item array")

    n = len(weight)
    return max_profit_in_01knapsack(weight, value, capacity, n)  # n will behave as index


if __name__ == "__main__":
    wt = [1, 3, 4, 5]
    val = [1, 4, 5, 7]
    c = 7

    # wt = [4, 5, 1]
    # val = [1, 2, 3]
    # c = 4

    # wt = [4, 5, 6]
    # val = [1, 2, 3]
    # c = 3

    print(solve_01knapsack(wt, val, c))
