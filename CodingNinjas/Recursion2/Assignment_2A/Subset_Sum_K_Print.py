from typing import List

from Utils.Array import print_array_inline

"""
This, problem is extension over the subset problem (under input-output method),
In this problem, we just need to add one more logic in the input-output diagram
"""

"""
Doing index Implementation - Forward only
We can't do Backward here, because of question requirements, we need to maintain the order if input
"""


def subset_sum_k(k: int, input: list, output: list, index: int) -> None:
    # Base Case 1
    if k == 0:
        print_array_inline(output)  # Directly printing it  Notice
        return

    # Base Case 2
    if index >= len(input):  # Don't proceed further
        return

    curr_element = input[index]

    if curr_element <= k:  # Have both options, Include it & Excluding it
        # Excluding it
        output_when_excluding = list.copy(output)
        subset_sum_k(k, input, output_when_excluding, index + 1)  # input, output changed, not k

        # Including It
        output_when_including = list.copy(output)
        output_when_including.append(curr_element)  # output, input & k changed
        subset_sum_k(k - curr_element, input, output_when_including, index + 1)

    else:  # Excluding it       if > k
        output_when_excluding = list.copy(output)
        subset_sum_k(k, input, output_when_excluding, index + 1)  # input, output changed, not k
    pass


def print_subsets_with_sum_k(arr: list, k: int) -> None:
    subset_sum_k(k, arr, [], 0)


if __name__ == '__main__':
    size = input()
    array = list(map(int, input().strip().split(" ")))
    k = int(input())
    print_subsets_with_sum_k(array, k)
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
