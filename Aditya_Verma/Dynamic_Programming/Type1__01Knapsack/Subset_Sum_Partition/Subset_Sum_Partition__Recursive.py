from Aditya_Verma.Dynamic_Programming.Type1__01Knapsack.Subset_Sum.Subset_Sum__Recursion__Idx_impl_backward import \
    solve_subsetsum


def solve_subsetsum_partition(nums):
    total_sum = sum(nums)
    if total_sum % 2 == 1:  # Odd
        return False

    s = total_sum // 2
    return solve_subsetsum(nums, s)


if __name__ == "__main__":
    print(solve_subsetsum_partition([1, 5, 11, 5]))
    print(solve_subsetsum_partition([1, 5, 3]))
