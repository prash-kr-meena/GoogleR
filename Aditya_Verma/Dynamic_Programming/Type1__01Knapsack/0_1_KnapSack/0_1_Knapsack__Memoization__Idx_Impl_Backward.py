# Here, we are using index to traverse the array, But we are doing it in the reverse order
# Returns: an int denoting the maximum profit, that can be achieved
from Utils.Matrix import get_filled_matrix


def max_profit_in_01knapsack(weight, value, capacity, n, dp) -> int:
    # Base Case
    if n == 0 or capacity == 0:
        return 0  # Max Profit that can be generated with these inputs will be 0

    if dp[n][capacity] != -1:
        return dp[n][capacity]

    # choosing the current item from end of the list
    curr_item_wt = weight[n - 1]
    curr_item_val = value[n - 1]

    if curr_item_wt <= capacity:
        # We have option for choosing it and not choosing it
        profit_after_choosing_curr_item = curr_item_val + \
                                          max_profit_in_01knapsack(weight, value, capacity - curr_item_wt, n - 1, dp)
        profit_after_NOT_choosing_curr_item = max_profit_in_01knapsack(weight, value, capacity, n - 1, dp)
        dp[n][capacity] = max(profit_after_choosing_curr_item, profit_after_NOT_choosing_curr_item)
        return dp[n][capacity]
    else:
        # We can't choose it
        profit_after_NOT_choosing_curr_item = max_profit_in_01knapsack(weight, value, capacity, n - 1, dp)
        dp[n][capacity] = profit_after_NOT_choosing_curr_item
        return dp[n][capacity]


def solve_01knapsack(weight, value, capacity):
    if len(weight) != len(value):
        raise ValueError("Invalid Item array")

    n = len(weight)
    dp = get_filled_matrix(row_size=len(weight) + 1, col_size=capacity + 1, fill=-1)
    return max_profit_in_01knapsack(weight, value, capacity, n, dp)  # n will behave as index


if __name__ == "__main__":
    # wt = [1, 3, 4, 5]
    # val = [1, 4, 5, 7]
    # c = 7

    # wt = [4, 5, 1]
    # val = [1, 2, 3]
    # c = 4

    # wt = [4, 5, 6]
    # val = [1, 2, 3]
    # c = 3

    wt = [83, 84, 85, 76, 13, 87, 2, 23, 33, 82, 79, 100, 88, 85, 91, 78, 83, 44, 4, 50, 11, 68, 90, 88, 73, 83, 46, 16,
          7, 35, 76, 31, 40, 49, 65, 2, 18, 47, 55, 38, 75, 58, 86, 77, 96, 94, 82, 92, 10, 86, 54, 49, 65, 44, 77, 22,
          81, 52]
    val = [57, 95, 13, 29, 1, 99, 34, 77, 61, 23, 24, 70, 73, 88, 33, 61, 43, 5, 41, 63, 8, 67, 20, 72, 98, 59, 46, 58,
           64, 94, 97, 70, 46, 81, 42, 7, 1, 52, 20, 54, 81, 3, 73, 78, 81, 11, 41, 45, 18, 94, 24, 82, 9, 19, 59, 48,
           2, 72]
    c = 41

    print(solve_01knapsack(wt, val, c))
