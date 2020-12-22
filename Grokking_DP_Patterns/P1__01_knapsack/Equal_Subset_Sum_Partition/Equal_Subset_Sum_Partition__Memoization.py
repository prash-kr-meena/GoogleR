def can_partition(num):
    s = sum(num)
    if s % 2 != 0:  # if 's' is a an odd number, we can't have two subsets with equal sum
        return False

    # initialize the 'dp' array, -1 for default, 1 for true and 0 for false
    dp = [[None for x in range(int(s / 2) + 1)] for y in range(len(num))]  # <<<<<<<<<<<

    return can_partition_recursive(dp, num, int(s / 2), 0)


def can_partition_recursive(dp, num, sum, current_index):
    if sum == 0:  # base check
        return True

    n = len(num)
    if n == 0 or current_index >= n:
        return False

    # if we have already processed a similar problem
    if dp[current_index][sum] is not None:
        return dp[current_index][sum]

    # recursive call after choosing the number at the current_index
    # if the number at current_index exceeds the sum, we shouldn't process this
    if num[current_index] <= sum:
        dp[current_index][sum] = can_partition_recursive(dp, num, sum - num[current_index], current_index + 1)
        if dp[current_index][sum] is True:  # if found the possibility to be True, then Why to process further
            return True

    # recursive call after excluding the number at the current_index
    dp[current_index][sum] = can_partition_recursive(dp, num, sum, current_index + 1)
    return dp[current_index][sum]


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
