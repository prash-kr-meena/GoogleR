"""
NGL  |  Nearest Greater to left
"""


def ngl_brute_force(nums):
    print("Brute Force Solution : ")
    length = len(nums)
    result = [-1] * length

    for i in range(0, length):
        for j in range(i - 1, -1, -1):  # from i-1 to 0     in reverse
            if nums[j] > nums[i]:  # First greater element, we could find in the left array
                result[i] = nums[j]
                break

    print(nums)
    print(result)
    return result


# You can remove the first two if's, that will work too
# Optimized stack solution
# O(n) Time
# O(n) Space
def nearest_greater_to_left(nums):
    print("\nOptimized Stack Solution : ")
    length = len(nums)
    result = [-1] * len(nums)  # Initializing all with -1 already
    stack = []  # Using list as stack

    for i in range(0, length):  # Only Change
        curr = nums[i]

        if len(stack) == 0:
            result[i] = -1  # result is -1

        elif len(stack) != 0 and stack[-1] > curr:
            result[i] = stack[-1]  # result is stack_top

        elif len(stack) != 0 and stack[-1] <= curr:
            while len(stack) != 0 and stack[-1] <= curr:
                stack.pop()  # pop stack_top till they are smaller then current

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
    ngl_brute_force(arr)
    nearest_greater_to_left(arr)

"""
10 5 11 10 20 12
"""
