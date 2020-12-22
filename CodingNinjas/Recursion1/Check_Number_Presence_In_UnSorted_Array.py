from sys import setrecursionlimit

'''
Basically implementing linear search using recursion, as array is not guaranteed to be sorted

Time : O(N)
Space : O(N)  for function stack frames, due to recursion
'''


# Index based implementation - backward
def recursive_linear_search(nums, key, n) -> bool:
    # Base Case
    if n == 0:
        return False  # Array exhausted but, element was not found

    #  Induction
    if nums[n - 1] == key:  # check with last element of the array
        return True

    # Hypothesis
    return recursive_linear_search(nums, key, n - 1)  # called on smaller input


def check_number(nums, key) -> bool:
    return recursive_linear_search(nums, key, len(nums))


if __name__ == "__main__":
    setrecursionlimit(11000)
    n = int(input())
    arr = list(map(int, input().strip().split(' ')))
    x = int(input())

    print(check_number(arr, x))
