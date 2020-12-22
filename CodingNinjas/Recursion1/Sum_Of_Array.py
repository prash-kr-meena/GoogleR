from sys import setrecursionlimit

'''
Hypothesis-Induction Method
Time  : O(n)  one direction recursion tree, no branching
Space : O(n)  due to recursion, function stacks
'''


# return sum(nums)      # short cut Note
# doing index, implementation -- Reverse Order
def sum_array(nums, n) -> int:
    # Base Case
    if n == 0:
        return 0

    # Hypothesis
    last_element = nums[n - 1]
    sum_of_smaller_array = sum_array(nums, n - 1)  # calling on smaller input

    # Induction
    return sum_of_smaller_array + last_element


# length based implementation -- Reverse Order
def sum_array__len_impl(nums) -> int:
    n = len(nums)
    # Base Case
    if n == 0:
        return 0

    # Hypothesis
    last_element = nums[n - 1]
    sum_of_smaller_array = sum_array__len_impl(nums[:n - 1])  # removing the last element, for next recursion call

    # Induction
    return sum_of_smaller_array + last_element


if __name__ == "__main__":
    setrecursionlimit(11000)
    n = int(input())
    arr = list(int(i) for i in input().strip().split(' '))

    print(sum_array(arr, len(arr)))
    print(sum_array__len_impl(arr))
