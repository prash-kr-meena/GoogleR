def count_ways_to_achieve_target_sum(nums, sum, curr_index):
    # base case
    if curr_index == len(nums) and sum == 0:  # we have reached last element and the sum has become 0
        # thi is correct base case
        return 1
        pass

    if curr_index >= len(nums) and sum != 0:
        return 0

    # if sum == 0:  # false case, eg [3 3 1 1] here it could be that we do 3 and -3 to get sum 0 and dont even process the array further

    count_ways_to_achieve_target_sum_after_changing_curr_num_sign = \
        count_ways_to_achieve_target_sum(nums, sum - nums[curr_index], curr_index + 1)

    count_ways_to_achieve_target_sum_after_taking_the_num_as_it_is = \
        count_ways_to_achieve_target_sum(nums, sum, curr_index + 1)

    return count_ways_to_achieve_target_sum_after_changing_curr_num_sign + count_ways_to_achieve_target_sum_after_taking_the_num_as_it_is


def target_sum(nums, sum):
    # edge case
    if nums is None or len(nums) == 0:
        return 0

    return count_ways_to_achieve_target_sum(nums, sum, 0)


def main():
    print(target_sum([1, 1, 2, 3], 1))


main()
