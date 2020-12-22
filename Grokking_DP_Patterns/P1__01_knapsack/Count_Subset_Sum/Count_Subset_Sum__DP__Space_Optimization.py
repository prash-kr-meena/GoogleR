def count_subsets(num, sum):
    n = len(num)
    dp = [0 for x in range(sum + 1)]
    dp[0] = 1

    # with only one number, we can form a subset only when the required sum is equal to the number
    for s in range(1, sum + 1):
        dp[s] = 1 if num[0] == s else 0

    # process all subsets for all sums
    for i in range(1, n):
        for s in range(sum, -1, -1):
            if s >= num[i]:
                dp[s] += dp[s - num[i]]

    return dp[sum]


def main():
    print("Total subsets : ", count_subsets([1, 1, 2, 3], 4))
    print("Total subsets : ", count_subsets([1, 2, 7, 1, 5], 9))


main()
