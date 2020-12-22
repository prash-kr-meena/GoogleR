# Recursion1 using input-output method
# The choice diagram is same as of 01 knapsack
def count_subsetsum(nums, sum, n) -> int:
    # Base Case
    if n == 0 and sum != 0:
        return 0  # can't form any subset

    if sum == 0:  # empty subset, regardless of n==0 or n!=0
        return 1

    # Choice Diagram
    if nums[n - 1] <= sum:  # Two choices
        subset_sum_count__when_including_curr_num = count_subsetsum(nums, sum - nums[n - 1], n - 1)
        subset_sum_count__when_NOT_including_curr_num = count_subsetsum(nums, sum, n - 1)
        return subset_sum_count__when_including_curr_num + subset_sum_count__when_NOT_including_curr_num
    else:  # Once Choice
        return count_subsetsum(nums, sum, n - 1)  # subset_sum_count__when_NOT_including_curr_num


def solve_subsetsum_count(nums, sum):
    n = len(nums)
    return count_subsetsum(nums, sum, n)


if __name__ == "__main__":
    print(solve_subsetsum_count([1, 2, 3, 3], 6))
    print(solve_subsetsum_count([1, 1, 1, 1], 1))
