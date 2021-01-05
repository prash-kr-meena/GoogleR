"""
NGR     |     Nearest Greater to right     |     Next Largest Element (GfG)

GFG Problem : https://practice.geeksforgeeks.org/problems/next-larger-element-1587115620/1
This solution is even accepted in GFG
"""


# You can remove the first two if's, that will work too
# Optimized stack solution
# O(n) Time
# O(n) Space
def next_greatest_element_to_right(nums):
    print("Optimized Stack Solution : ")
    length = len(nums)
    result = [-1] * len(nums)  # Initializing all with -1 already

    stack = []  # Using list as stack

    for i in range(length - 1, -1, -1):  # n-1 to 0 in reverse
        curr = nums[i]
        while len(stack) != 0 and stack[-1] <= curr:
            stack.pop()  # pop all elements smaller then equal to curr, unless the stack is empty

        # By which of the above condition, the loop has ended
        if len(stack) == 0:
            result[i] = -1  # result is -1                similar to our 1st condition
        else:  # found an element greater then curr_element
            result[i] = stack[-1]  # result is stack_top          similar to our 2nd condition

        # Handled the current element, We have processed it
        stack.append(curr)

    print(nums)
    print(result)
    return result


if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    next_greatest_element_to_right(arr)
