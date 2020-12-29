from sys import setrecursionlimit
from typing import List

from Utils.Array import print_array_inline

'''
Here traversing from front or end both are acceptable as in either case we need to travel the whole array,

NOTE : both implementations are index based

The base implementation used here is from the Find_First_Occurrence.py Problem

Time : O(n)
Space : O(n) for storing indices + O(n) due to recursion
'''


def find_all_occurrence__forward(nums, key, index, all_indices) -> None:
    # Base Case
    if index >= len(nums):
        return  # Exhausted the array

    # Induction
    if nums[index] == key:  # Here we don't traverse full array if we find the match initially
        all_indices.append(index)

    # Hypothesis
    find_all_occurrence__forward(nums, key, index + 1, all_indices)


def find_index_of_all_occurrence__forward(nums, key, ) -> List[int]:
    all_indices = []
    find_all_occurrence__forward(nums, key, 0, all_indices)
    return all_indices


#  ---------------------------------------------------------

def find_all_occurrence__backward(nums, key, n, all_indices) -> None:
    # Base Case
    if n == 0:
        return  # Exhausted the array

    # Hypothesis
    find_all_occurrence__backward(nums, key, n - 1, all_indices)

    # Induction
    if nums[n - 1] == key:  # last element is similar to key
        all_indices.append(n - 1)


def find_index_of_all_occurrence__backward(nums, key) -> List[int]:
    all_indices = []
    find_all_occurrence__backward(nums, key, len(nums), all_indices)
    return all_indices


if __name__ == "__main__":
    setrecursionlimit(11000)
    n = int(input())
    arr = list(int(i) for i in input().strip().split(' '))
    x = int(input())

    print_array_inline(find_index_of_all_occurrence__forward(arr, x))
    print_array_inline(find_index_of_all_occurrence__backward(arr, x))

'''
4
9 8 10 8
8


5
9 8 10 8 8
8
'''
