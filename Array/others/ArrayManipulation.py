# https://www.hackerrank.com/challenges/crush/problem
"""
Prerequisite to solve this problem : PrefixSum
"""


# Complete the arrayManipulation function below.
# Index is 1_based : so creating n+1 size
# Now due to our implementation we would require 1 more index so doing n+2
def array_manipulation(n, queries) -> int:
    length = n + 2
    arr = [0] * length

    for query in queries:
        left, right, value = query[0], query[1], query[2]
        # Logic to help in prefix-sum algorithm
        arr[left] += value  # Adding   value to idx_left
        arr[right + 1] -= value  # Adding (-value) to idx_right+1

    # Applying pre-fix algorithm  AND  at the same time also getting the max
    maximum = float("-inf")
    for i in range(1, length):
        arr[i] = arr[i] + arr[i - 1]
        maximum = max(maximum, arr[i])

    # print(arr)
    return maximum


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().strip().split())))

    result = array_manipulation(n, queries)
    print(result)

"""
Input
5 3
1 2 100
2 5 100
3 4 100

Output
200


"""
