def can_partition(num):
    s = sum(num)
    dp = [[-1 for x in range(s + 1)] for y in range(len(num))]
    return can_partition_recursive(dp, num, 0, 0, 0)


def can_partition_recursive(dp, num, current_index, sum_A, sum_B):
    if current_index == len(num):  # base check
        return abs(sum_A - sum_B)

    # check if we have already processed similar problem
    if dp[current_index][sum_A] != -1:
        return dp[current_index][sum_A]

    # recursive call after including the number at the currentIndex in the first set
    diff1 = can_partition_recursive(dp, num, current_index + 1, sum_A + num[current_index], sum_B)

    # recursive call after including the number at the currentIndex in the second set
    diff2 = can_partition_recursive(dp, num, current_index + 1, sum_A, sum_B + num[current_index])

    dp[current_index][sum_A] = min(diff1, diff2)
    return dp[current_index][sum_A]


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()
