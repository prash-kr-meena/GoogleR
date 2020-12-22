from sys import setrecursionlimit

from Final450.Searching_Sorting._Named_Algorithms.binary_search_recursive import binary_search_recursive

'''
Basically implementing Binary Search using recursion, as array is guaranteed to be sorted

Time : O(log N)
Space : O(log N)  for function stack frames, due to recursion
'''


def check_number(nums, key) -> bool:
    index = binary_search_recursive(nums, key)
    return index != -1


if __name__ == "__main__":
    setrecursionlimit(11000)
    n = int(input())
    arr = list(map(int, input().strip().split(' ')))
    x = int(input())

    print(check_number(arr, x))

'''


7
1 3 5 9 9 18 20
1


7
1 3 5 9 9 18 20
9
^
 \__ Just change the search value heres
'''
