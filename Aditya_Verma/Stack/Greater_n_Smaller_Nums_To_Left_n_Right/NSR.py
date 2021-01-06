"""
 NSL  |  Nearest Smaller to Right
"""


# You can remove the first two if's, that will work too

# Optimized stack solution
# O(n) Time
# O(n) Space
def nearest_smaller_to_right(nums):
    print("\nOptimized Stack Solution : ")
    length = len(nums)
    result = [-1] * length
    stack = []  # using list as stack

    for i in range(length - 1, -1, -1):  # n-1 to 0 in reverse
        curr = nums[i]

        if len(stack) == 0:
            result[i] = -1  # result is -1, when stack is empty

        elif len(stack) != 0 and stack[-1] < curr:  # stack_top < curr element
            result[i] = stack[-1]  # result is stack_top

        elif len(stack) != 0 and stack[-1] >= curr:  # stack_top >= curr element
            while len(stack) != 0 and stack[-1] >= curr:
                stack.pop()  # pop all the elements greater then equal to curr, unless the stack is empty

            # By which of the above condition, the loop has ended
            if len(stack) == 0:
                result[i] = -1  # result is -1                similar to our 1st condition
            else:
                result[i] = stack[-1]  # result is stack_top          similar to our 2nd condition

        # Handled the current element, as we have processed it
        stack.append(curr)

    print(nums)
    print(result)
    return result


if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    nearest_smaller_to_right(arr)

"""
2 1 3 4
4 5 2 10 8
"""
