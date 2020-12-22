def count_subsets(nums, sum):
    n = len(nums)
    dp = [[-1 for x in range(sum + 1)] for y in range(n)]

    # populate the sum = 0 columns, as we will always have an empty set for zero sum
    for i in range(0, n):
        dp[i][0] = 1

    # with only one number, we can form a subset only when the required sum is equal to its value
    for s in range(1, sum + 1):
        dp[0][s] = 1 if nums[0] == s else 0  # Note <<<   0's

    # process all subsets for all sums
    for i in range(1, n):
        for s in range(1, sum + 1):
            count_by_excluding = dp[i - 1][s]  # exclude the number

            count_by_including = 0
            if s >= nums[i]:  # include the number, if it does not exceed the sum
                count_by_including = dp[i - 1][s - nums[i]]

            dp[i][s] = count_by_including + count_by_excluding

    return dp[n - 1][sum]  # the bottom-right corner will have our answer.


def main():
    print("Total subsets : ", count_subsets([1, 1, 2, 3], 4))
    print("Total subsets : ", count_subsets([1, 2, 7, 1, 5], 9))


main()
