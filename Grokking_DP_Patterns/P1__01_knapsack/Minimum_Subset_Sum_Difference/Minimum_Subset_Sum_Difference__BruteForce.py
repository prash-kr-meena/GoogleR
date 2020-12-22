def can_partition(nums):
    if nums is None or len(nums) == 0:  # Edge case
        return float("inf")  # -- My Code --

    return can_partition_recursive(nums, 0, 0, 0)


def can_partition_recursive(nums, current_index, sum_A, sum_B):
    if current_index == len(nums):  # base check
        return abs(sum_A - sum_B)

    # recursive call after including the number at the currentIndex in the first set
    diff1 = can_partition_recursive(nums, current_index + 1, sum_A + nums[current_index], sum_B)

    # recursive call after including the number at the currentIndex in the second set
    diff2 = can_partition_recursive(nums, current_index + 1, sum_A, sum_B + nums[current_index])

    return min(diff1, diff2)


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()
