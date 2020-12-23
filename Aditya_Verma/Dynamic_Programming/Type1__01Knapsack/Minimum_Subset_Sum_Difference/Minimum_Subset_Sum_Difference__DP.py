from Aditya_Verma.Dynamic_Programming.Type1__01Knapsack.Subset_Sum.Subset_Sum__DP__Backward__Return_Table import \
    subset_sum__table


def minimum_subset_sum_difference(nums) -> int:
    n = len(nums)
    sum_range = sum(nums)
    dp = subset_sum__table(nums, sum_range)
    # formula
    # sum_range-2*(s)

    mid_range = sum_range // 2

    for j in range(mid_range, -1, -1):  # going reverse   Note # Including 0th
        # for the first jth element in reverse, will be our maximum so that we can minimize (sum_range - 2*sumbset_sum)
        if dp[n][j]:
            return sum_range - 2 * j  # j denotes the sum, ie, columns value


if __name__ == "__main__":
    print(minimum_subset_sum_difference([1, 6, 11, 5]))
    print(minimum_subset_sum_difference([1, 4]))
    print(minimum_subset_sum_difference([10000]))
