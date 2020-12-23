from Aditya_Verma.Dynamic_Programming.Type1__01Knapsack.Subset_Sum.Subset_Sum__DP__Backward import subset_sum


# Note : exact same code, only module change

def solve_subsetsum_partition(nums):
    total_sum = sum(nums)
    if total_sum % 2 == 1:  # Odd
        return False

    s = total_sum // 2
    return subset_sum(nums, s)


if __name__ == "__main__":
    print(solve_subsetsum_partition([1, 5, 11, 5]))
    print(solve_subsetsum_partition([1, 5, 3]))
