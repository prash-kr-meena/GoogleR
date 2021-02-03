# Here, we are using index to traverse the array, But we are doing it in the reverse order
# Returns: an int denoting the maximum profit, that can be achieved
from Utils.Array import input_array


def max_profit_in_01knapsack(weight, value, capacity, n) -> int:
    # Base Case --> Initialization step
    """
    for i in range(n + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
    """
    dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    # Starting from 1st index, not 0
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            curr_item_wt = weight[i - 1]
            curr_item_val = value[i - 1]

            if curr_item_wt <= j:
                # We have option for choosing it and not choosing it
                profit_after_choosing_curr_item = curr_item_val + dp[i - 1][j - curr_item_wt]
                profit_after_NOT_choosing_curr_item = dp[i - 1][j]
                dp[i][j] = max(profit_after_choosing_curr_item, profit_after_NOT_choosing_curr_item)
            else:
                # We can't choose it
                profit_after_NOT_choosing_curr_item = dp[i - 1][j]
                dp[i][j] = profit_after_NOT_choosing_curr_item

    return dp[n][capacity]


if __name__ == "__main__":
    wt = input_array()
    val = input_array()
    c = int(input("capacity : "))
    print(max_profit_in_01knapsack(wt, val, c, len(wt)))

"""
wt  = 1  3  4  5
val = 1  4  5  7
c   = 7

wt  = 83  84  85  76  13  87  2  23  33  82  79  100  88  85  91  78  83  44  4  50  11  68  90  88  73  83  46  16 7  35  76  31  40  49  65  2  18  47  55  38  75  58  86  77  96  94  82  92  10  86  54  49  65  44  77  22 81  52
val = 57  95  13  29  1  99  34  77  61  23  24  70  73  88  33  61  43  5  41  63  8  67  20  72  98  59  46  58  64  94  97  70  46  81  42  7  1  52  20  54  81  3  73  78  81  11  41  45  18  94  24  82  9  19  59  48  2  72
c   = 41
"""
