from Array._Algorithms.PrefixSum import prefix_sum
from Utils.Array import input_array

"""
https://www.geeksforgeeks.org/range-sum-queries-without-updates/
With this approach, of prefix-sum this problem can be solved in O(n+m) time
Otherwise the brute force solution would be o(m*n)
    -> as for m queries we would be doing O(n) operations in worst case 



here, Assuming that the left and right indexes are given by 0-indexing
"""


def range_sum_queries_without_updates(arr, queries) -> None:
    sum_arr = prefix_sum(arr)
    print(queries)
    for query in queries:
        left = query[0]
        right = query[1]

        if left == 0:  # ie summing from star
            print(sum_arr[right])
        else:
            print(sum_arr[right] - sum_arr[left - 1])

    pass


if __name__ == '__main__':
    array = input_array()

    m = int(input("no of query: "))
    queries = []  # To store m queries
    for i in range(m):
        query = tuple(map(int, input("query : ").strip().split()))
        queries.append(query)

    range_sum_queries_without_updates(array, queries)

"""
6 3 -2 4 -1 0 -5
2
0 4
1 2

1 2 3 4 5
2
0 4
1 2


1 2 3 4 5
2 3
2 4

"""
