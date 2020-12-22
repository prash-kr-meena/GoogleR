# Recursion1 using input-output method
# The choice diagram is same as of 01 knapsack
def subsetsum(nums, sum, n) -> bool:
    # Base Case
    if n == 0 and sum > 0:
        return False
    if sum == 0:
        return True

    if nums[n - 1] <= sum:
        # subsetsum_possible_if_including_curr_num or subsetsum_possible_if_NOT_including_curr_num
        return subsetsum(nums, sum - nums[n - 1], n - 1) or subsetsum(nums, sum, n - 1)
    else:
        # subsetsum_possible_if_NOT_including_curr_num
        return subsetsum(nums, sum, n - 1)


def solve_subsetsum(nums, sum):
    return subsetsum(nums, sum, len(nums))


if __name__ == "__main__":
    print(solve_subsetsum([3, 34, 4, 12, 5, 2], 9))
    print(solve_subsetsum([3, 34, 4, 12, 5, 2], 30))
