from Utils.Array import input_array
from Utils.Matrix import get_filled_matrix


# Here, we are using index to traverse the array, and we are going in forward direction
# Returns: an int denoting the maximum profit, that can be achieved
def max_profit_in_01knapsack(weight, value, capacity, index, dp) -> int:
    size = len(weight)
    # Base Case
    if index >= size or capacity == 0:
        return 0  # Max Profit that can be generated with these inputs will be 0

    if dp[index][capacity] != -1:
        return dp[index][capacity]

    # choosing the current item from end of the list
    curr_item_wt = weight[index]
    curr_item_val = value[index]

    # We are shortening the input, ie weight and value, using index
    if curr_item_wt <= capacity:
        # We have option for choosing it and not choosing it
        profit_after_choosing_curr_item = curr_item_val + \
                                          max_profit_in_01knapsack(weight, value, capacity - curr_item_wt, index + 1,
                                                                   dp)
        profit_after_NOT_choosing_curr_item = max_profit_in_01knapsack(weight, value, capacity, index + 1, dp)
        dp[index][capacity] = max(profit_after_choosing_curr_item, profit_after_NOT_choosing_curr_item)
        return dp[index][capacity]
    else:
        # We can't choose it
        profit_after_NOT_choosing_curr_item = max_profit_in_01knapsack(weight, value, capacity, index + 1, dp)
        dp[index][capacity] = profit_after_NOT_choosing_curr_item
        return dp[index][capacity]


def solve_01knapsack(weight, value, capacity):
    if len(weight) != len(value):
        raise ValueError("Invalid Item array")

    dp = get_filled_matrix(row_size=len(weight) + 1, col_size=capacity + 1, fill=-1)
    return max_profit_in_01knapsack(weight, value, capacity, 0, dp)


if __name__ == "__main__":
    wt = input_array()
    val = input_array()
    c = int(input("capacity : "))
    print(solve_01knapsack(wt, val, c))
