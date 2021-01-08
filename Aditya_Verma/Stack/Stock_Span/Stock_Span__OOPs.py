from Abstract_Data_Types.StackADT import StackADT

"""
Idea is to make it more object oriented solution
use stack ADT and make a pair class
"""


class Pair:
    def __init__(self, value, index):
        self._value = value  # Private
        self._index = index  # Private

    def get_value(self):
        return self._value

    def get_index(self):
        return self._index


def nearest_greater_element_index_to_left(nums):
    length = len(nums)
    result = [-1] * len(nums)
    stack = StackADT()

    for i in range(0, length):
        curr = nums[i]

        if stack.size() == 0:
            result[i] = -1

        elif stack.size() != 0 and stack.peek().get_value() > curr:  # comparing value Notice
            result[i] = stack.peek().get_index()  # putting index Notice

        elif stack.size() != 0 and stack.peek().get_value() <= curr:  # comparing value Notice
            while stack.size() != 0 and stack.peek().get_value() <= curr:  # comparing value Notice
                stack.pop()

            if stack.size() == 0:
                result[i] = -1
            else:
                result[i] = stack.peek().get_index()  # putting index Notice

        # Processed Curr
        stack.push(Pair(curr, i))  # Pair(value, index) Notice

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
