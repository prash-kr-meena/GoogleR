# You can remove the first two if's, that will work too
# Optimized stack solution
# O(n) Time
# O(n) Space
def indexes_of_next_smaller_element_to_right(nums):
    length = len(nums)
    result = [-1] * length  # Initializing all with -1 already
    stack = []  # Using list as stack

    for i in range(length - 1, -1, -1):  # n-1 to 0 in reverse
        curr = nums[i]

        if len(stack) == 0:
            result[i] = -1  # result is -1, when stack is empty

        elif stack[-1][0] < curr:  # stack_top < curr element       Notice : compare-value
            result[i] = stack[-1][1]  # result is stack_top         Notice : insert-index

        elif stack[-1][0] >= curr:  # stack_top >= curr element     Notice : compare-value
            while len(stack) != 0 and stack[-1][0] >= curr:  # Notice : compare-value
                stack.pop()  # pop all elements greater then equal to curr, until the stack is empty

            # By which of the above condition, the loop has ended
            if len(stack) == 0:
                result[i] = -1  # result is -1      <similar to our 1st condition>
            else:  # found an element smaller then curr_element
                result[i] = stack[-1][1]  # result is stack_top   <similar to our 2nd condition> Notice : insert-index

        # Handled the current element, We have processed it
        stack.append((curr, i))  # Notice  0: value, 1: index

    print(nums)
    print(result)
    return result


if __name__ == '__main__':
    buildings = list(map(int, input().strip().split()))
    indexes_of_next_smaller_element_to_right(buildings)

"""
6 2 5 4 5 1 6

[1, 5, 3, 5, 5, -1, -1]
"""
