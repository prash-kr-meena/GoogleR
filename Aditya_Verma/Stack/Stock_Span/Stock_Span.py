"""
comments removed, for better clarity, read them from NGL problem
Compare the solution with NGR, where it changes, I have marked Notice
"""


# You can remove the first two if's, that will work too
# Optimized stack solution
# O(n) Time
# O(n) Space
def nearest_greater_element_index_to_left(nums):
    length = len(nums)
    result = [-1] * length  # Initializing all with -1 already
    stack = []  # Using list as stack, stack of pair(value, index)

    for i in range(0, length):  # Going Forward
        curr = nums[i]

        if len(stack) == 0:
            result[i] = -1  # result is -1, when stack is empty

        elif stack[-1][0] > curr:  # stack_top (value part) > curr element      # 0:comparing value Notice
            result[i] = stack[-1][1]  # result is stack_top (index part)        # 1:putting index Notice

        elif stack[-1][0] <= curr:  # stack_top <= curr element     # 0:comparing value Notice
            while len(stack) != 0 and stack[-1][0] <= curr:  # 0:comparing value Notice
                stack.pop()  # pop all elements smaller then equal to curr, until the stack is empty

            # By which of the above condition, the loop has ended
            if len(stack) == 0:
                result[i] = -1  # result is -1            similar to our 1st condition
            else:  # found an element greater then curr_element
                result[i] = stack[-1][1]  # result is stack_top (index part)      similar to our 2nd condition
                # 1:putting index Notice

        # Handled the current element, We have processed it
        stack.append((curr, i))  # added pair (element, its_index) Notice       0:element   1:index

    print(nums, "<- original")
    print(result, "<- ngl index")
    return result


def get_result_array(ngl_index_array):
    length = len(ngl_index_array)
    res = [-1] * length

    for i in range(0, length):
        res[i] = i - ngl_index_array[i]

    return res


if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    ngl_index_array = nearest_greater_element_index_to_left(arr)
    print(get_result_array(ngl_index_array))

"""
10 5 11 10 20 12
100 80 60 70 60 75 85
"""
