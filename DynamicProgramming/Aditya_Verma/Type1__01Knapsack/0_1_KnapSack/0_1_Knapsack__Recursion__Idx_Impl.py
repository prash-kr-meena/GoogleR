from Utils.Array import input_array


# Here, we are using index to traverse the array, and we are going in forward direction
# Returns: an int denoting the maximum profit, that can be achieved
def max_profit_in_01knapsack(weight, value, capacity, index=0) -> int:
    # Base Case
    if index >= len(weight) or capacity == 0:
        return 0  # Max Profit that can be generated with these inputs will be 0

    # choosing the current item from end of the list
    curr_item_wt = weight[index]
    curr_item_val = value[index]

    # We are shortening the input, ie weight and value, using index
    if curr_item_wt <= capacity:
        # We have option for choosing it and not choosing it
        profit_after_choosing_curr_item = curr_item_val + \
                                          max_profit_in_01knapsack(weight, value, capacity - curr_item_wt, index + 1)
        profit_after_NOT_choosing_curr_item = max_profit_in_01knapsack(weight, value, capacity, index + 1)
        return max(profit_after_choosing_curr_item, profit_after_NOT_choosing_curr_item)
    else:
        # We can't choose it
        profit_after_NOT_choosing_curr_item = max_profit_in_01knapsack(weight, value, capacity, index + 1)
        return profit_after_NOT_choosing_curr_item


def solve_01knapsack(weight, value, capacity):
    if len(weight) != len(value):
        raise ValueError("Invalid Item array")

    return max_profit_in_01knapsack(weight, value, capacity, 0)


if __name__ == "__main__":
    wt = input_array()
    val = input_array()
    c = int(input("capacity : "))
    print(solve_01knapsack(wt, val, c))

"""
wt  = 1 3 4 5
val = 1 4 5 7
c  =  7

wt  = 4 5 1
val = 1 2 3
c  =  4

wt  = 4 5 1
val = 1 2 3
c  =  3
"""
