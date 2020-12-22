def count_subset_sum(nums, sum, curr_index) -> int:  # s -> sum
    if sum == 0:  # Base case 1   This should be put before the other base case  <<< NOTE <<_IMPORTANT_>>
        return 1

    if curr_index >= len(nums):  # Base case 2
        return 0

    # recursive call after selecting the number at the currentIndex
    # if the number at currentIndex exceeds the sum, we shouldn't process this
    subset_count_by_including_curr_element = 0
    if nums[curr_index] <= sum:
        subset_count_by_including_curr_element = count_subset_sum(nums, sum - nums[curr_index], curr_index + 1)

    # recursive call after excluding the number at the currentIndex
    subset_count_by_excluding_curr_element = count_subset_sum(nums, sum, curr_index + 1)

    return subset_count_by_including_curr_element + subset_count_by_excluding_curr_element


def solve_count_subset_sum(nums, s) -> int:  # s -> sum
    # Edge cases
    if nums is None or len(nums) == 0:
        return 0

    return count_subset_sum(nums, s, 0)


def main():
    print("Total subsets : ", solve_count_subset_sum([1, 1, 2, 3], 4))
    print("Total subsets : ", solve_count_subset_sum([1, 2, 7, 1, 5], 9))


main()
