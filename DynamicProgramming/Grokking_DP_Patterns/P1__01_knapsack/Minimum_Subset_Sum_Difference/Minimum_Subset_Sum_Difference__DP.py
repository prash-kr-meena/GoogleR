def can_partition(num):
    s = sum(num)
    n = len(num)

    column_size = s // 2 + 1  # s // 2 + 1 --> as sum can be odd here
    dp = [[False for x in range(column_size)] for y in range(n)]

    # populate the s=0 columns, as we can always form '0' sum with an empty set
    for i in range(0, n):
        dp[i][0] = True

    # with only one number, we can form a subset only when the required sum is equal to that number
    # dp[0][num[0]]    # Note <<<< one liner, O(1)
    for j in range(1, column_size):
        dp[0][j] = num[0] == j

    # process all subsets for all sums
    for i in range(1, n):
        for j in range(1, column_size):
            if dp[i - 1][j]:
                # if we can get the sum 's' without the number at index 'i'
                dp[i][j] = dp[i - 1][j]
            elif num[i] <= j:
                # else include the number and see if we can find a subset to get the remaining sum
                dp[i][j] = dp[i - 1][j - num[i]]
            # else: False By default        <<<<<

    # find the largest index in the last row which is true,
    # ie basically first True that you find while going reverse in the last row
    sum_A = 0
    last_row = n - 1
    for col in range(column_size - 1, -1, -1):
        if dp[last_row][col]:
            sum_A = col
            break

    sum_B = s - sum_A
    return abs(sum_B - sum_A)


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()
