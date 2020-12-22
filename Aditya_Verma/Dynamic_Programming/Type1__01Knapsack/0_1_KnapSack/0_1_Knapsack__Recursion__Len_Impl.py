# Length base implementation
# Returns: an int denoting the maximum profit, that can be achieved
def max_profit_in_01knapsack(weight, value, capacity) -> int:
    n = len(weight)
    # Base Case
    if n == 0 or capacity == 0:
        return 0  # Max Profit that can be generated with these inputs will be 0

    # choosing the current item from end of the list
    curr_item_wt = weight[0]
    curr_item_val = value[0]

    # making the input smaller
    new_weight = weight[1:]
    new_value = value[1:]

    if curr_item_wt <= capacity:
        # We have option for choosing it and not choosing it
        profit_after_choosing_curr_item = curr_item_val + \
                                          max_profit_in_01knapsack(new_weight, new_value, capacity - curr_item_wt)
        profit_after_NOT_choosing_curr_item = max_profit_in_01knapsack(new_weight, new_value, capacity)
        return max(profit_after_choosing_curr_item, profit_after_NOT_choosing_curr_item)
    else:
        # We can't choose it
        profit_after_NOT_choosing_curr_item = max_profit_in_01knapsack(new_weight, new_value, capacity)
        return profit_after_NOT_choosing_curr_item


def solve_01knapsack(weight, value, capacity):
    if len(weight) != len(value):
        raise ValueError("Invalid Item array")

    return max_profit_in_01knapsack(weight, value, capacity)


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

"""
wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]
c = 7

wt = [4,5,1]
val = [1,2,3]
c = 4

wt = [4,5,1]
val = [1,2,3]
c = 3

"""
