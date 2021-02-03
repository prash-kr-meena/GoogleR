from sys import setrecursionlimit

'''
Here the question specifically mentioned to start from the left -> right
We will do both the implementation though

Here traversing from end (either iteratively or recursively) makes more sense as, 
then we can eliminate traversing over the whole array, if we have fond the element


NOTE : both implementations are index based

Time : O(n)
Space : O(n) due to recursion
'''


# This implementation is similar to the backward implementation of find_first_occurrence__backward
def find_last_occurrence__forward(nums, key, index) -> int:
    # Base Case
    if index >= len(nums):
        return -1  # Exhausted the array

    #  Hypothesis
    occurrence_index_smaller_array = find_last_occurrence__forward(nums, key, index + 1)

    # Induction
    if occurrence_index_smaller_array != -1:
        return occurrence_index_smaller_array
    elif nums[index] == key:
        return index
    else:
        return -1


def find_index_of_last_occurrence__forward(nums, key) -> int:
    return find_last_occurrence__forward(nums, key, 0)


# ------------------------------------------------------------

# This implementation is similar to the forward implementation of find_first_occurrence__forward
def find_last_occurrence__backward(nums, key, n) -> int:
    # Base Case
    if n == 0:
        return -1  # Fully exhausted the array (search space)

    # Induction
    if nums[n - 1] == key:  # nums[n - 1] is our last_number
        return n - 1

    # Hypothesis
    return find_last_occurrence__backward(nums, key, n - 1)  # last_occurrence_index_smaller_array


def find_index_of_last_occurrence__backward(nums, key) -> int:
    return find_last_occurrence__backward(nums, key, len(nums))


if __name__ == "__main__":
    setrecursionlimit(11000)
    n = int(input())
    arr = list(int(i) for i in input().strip().split(' '))
    x = int(input())

    print(find_index_of_last_occurrence__forward(arr, x))
    print(find_index_of_last_occurrence__backward(arr, x))

'''
4
9 8 10 8
8
'''
