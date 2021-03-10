from typing import List

from Utils.Array import input_array

"""
LeetCode : https://leetcode.com/problems/find-the-most-competitive-subsequence/
Youtube Video : https://www.youtube.com/watch?v=Ol7yz0XKKLw&t=26s&ab_channel=LeadCoding
"""


def find_lexicographically_smaller_subsequence_of_size_k(arr: List[int], k: int) -> List[int]:
    n = len(arr)
    no_of_elements_to_be_removed = n - k

    stack = []  # stack.append(), stack.pop(), stack[-1]

    for element in arr:
        if len(stack) == 0:  # empty
            stack.append(element)
            continue

        # before putting any element at the top, check if the top is larger then this element, and remove all of them
        while len(stack) != 0 and stack[-1] > element and no_of_elements_to_be_removed != 0:
            stack.pop()
            no_of_elements_to_be_removed -= 1  # update

        # and finally push it to stack, after you have removed or even if there was nothing to be removed
        stack.append(element)

    while len(stack) != 0 and no_of_elements_to_be_removed != 0:
        stack.pop()  # Remove all the un-removed extra elements from the stack top
        no_of_elements_to_be_removed -= 1

    # push all the stack elements to a list,
    result = []
    while len(stack) != 0:
        result.append(stack.pop())

    # These elements will be reverse order from what we require, so reverse the final result
    result.reverse()
    return result


if __name__ == '__main__':
    array = input_array()
    k_size = int(input())
    print(find_lexicographically_smaller_subsequence_of_size_k(array, k_size))

"""
2 4 3 3 5 4 9 6
4
"""

"""
3 5 2 6
2
"""

"""
71 18 52 29 55 73 24 42 66 8 80 2
3
"""
