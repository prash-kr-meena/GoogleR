from typing import List

from Utils.Matrix import print_matrix_beautiful

"""
This, problem is extension over the subset problem (under input-output method),
In this problem, we just need to add one more logic in the input-output diagram
"""

"""
Generally, we have our output:str but here as question requires us to return the subsets in list,
we will be using a list instead of str

NOTE::  as list is not immutable like string or tuple, it causes difficulty in implementation,
        as you then require to manually set and unset things
    ->  So on thing, you could do is instead of returning List[List], you could return List[str] or List[tuple]


Doing index Implementation - Forward only
We can't do Backward here, because of question requirements, we need to maintain the order if input
"""


def subset_sum_k(all_subsets_with_k_sum: List[list], k: int, input: list, output: list, index: int) -> None:
    # Base Case 1
    if k == 0:
        all_subsets_with_k_sum.append(output)  # Appending to bigger list Notice
        return

    # Base Case 2
    if index >= len(input):  # Don't proceed further
        return

    curr_element = input[index]

    if curr_element <= k:  # Have both options, Include it & Excluding it
        # Excluding it
        output_when_excluding = list.copy(output)
        subset_sum_k(all_subsets_with_k_sum, k, input, output_when_excluding, index + 1)  # input, output changed, not k

        # Including It
        output_when_including = list.copy(output)
        output_when_including.append(curr_element)  # output, input & k changed
        subset_sum_k(all_subsets_with_k_sum, k - curr_element, input, output_when_including, index + 1)

    else:  # Excluding it       if > k
        output_when_excluding = list.copy(output)
        subset_sum_k(all_subsets_with_k_sum, k, input, output_when_excluding, index + 1)  # input, output changed, not k
    pass


def get_subsets_with_sum_k(arr: list, k: int) -> List[list]:
    all_subsets_with_k_sum = []
    subset_sum_k(all_subsets_with_k_sum, k, arr, [], 0)
    return all_subsets_with_k_sum


if __name__ == '__main__':
    size = input()
    array = list(map(int, input().strip().split(" ")))
    k = int(input())
    print_matrix_beautiful(get_subsets_with_sum_k(array, k))
    pass

"""
Input :

9
5 12 3 17 1 18 15 3 17
6


4
1 1 2 3
3
"""
