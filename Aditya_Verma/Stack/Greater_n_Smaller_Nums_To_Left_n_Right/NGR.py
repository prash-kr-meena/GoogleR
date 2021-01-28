from typing import List

"""
NGR     |     Nearest Greater to right     |     Next Largest Element (GfG)
"""


# Brute Force Solution
# O(n2) Time
# O(1) Space
def ngr_brute_force(nums) -> List[int]:
    print("Brute Force Solution : ")
    length = len(nums)
    result = [-1] * length  # Initializing all with -1 already

    for i in range(0, length):
        for j in range(i + 1, length):  # j depends on i
            if nums[j] > nums[i]:  # First element that we found greater, is our next greater
                result[i] = nums[j]
                break  # Important, as we don't want to look more, once we find first element
    print(nums)
    print(result)
    return result


# You can remove the first two if's, that will work too
# Optimized stack solution
# O(n) Time
# O(n) Space
def next_greatest_element_to_right(nums):
    print("\nOptimized Stack Solution : ")
    length = len(nums)
    result = [-1] * length  # Initializing all with -1 already
    stack = []  # Using list as stack

    for i in range(length - 1, -1, -1):  # n-1 to 0 in reverse
        curr = nums[i]

        if len(stack) == 0:
            result[i] = -1  # result is -1, when stack is empty

        elif stack[-1] > curr:  # stack_top > curr element
            result[i] = stack[-1]  # result is stack_top

        elif stack[-1] <= curr:  # stack_top <= curr element
            while len(stack) != 0 and stack[-1] <= curr:
                stack.pop()  # pop all elements smaller then equal to curr, until the stack is empty

            # By which of the above condition, the loop has ended
            if len(stack) == 0:
                result[i] = -1  # result is -1      <similar to our 1st condition>
            else:  # found an element greater then curr_element
                result[i] = stack[-1]  # result is stack_top   <similar to our 2nd condition>

        # Handled the current element, We have processed it
        stack.append(curr)

    print(nums)
    print(result)
    return result


if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    ngr_brute_force(arr)
    next_greatest_element_to_right(arr)

"""
Input   1 3 2 4
Output  3 4 4 -1


Input   6 8 0 1 3
Output  8 -1 1 3 -1
"""
