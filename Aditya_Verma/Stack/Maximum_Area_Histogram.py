# # MAH   |   Maximum Area Of Histogram
#
# def indexes_of_next_smaller_element_to_right(nums) -> list:
#     length = len(nums)
#     result = [-1] * length
#     stack = []
#
#     for i in range(length - 1, -1, -1):
#         curr = nums[i]
#
#         if len(stack) == 0:  # Empty stack
#             result[i] = -1
#
#         elif stack[-1][0] < curr:
#             result[i] = stack[-1][1]
#
#         elif stack[-1][0] >= curr:  # stack top containing elements greater then curr
#             while len(stack) != 0 and stack[-1][0] >= curr:
#                 stack.pop()
#
#             if len(stack) == 0:
#                 result[i] = -1
#             else:  # still there is element which is smaller then curr
#                 result[i] = stack[-1][1]
#
#         # handled curr
#         stack.append((curr, i))  # 0:value & 1:index
#
#     return result
#
#
# def indexes_of_next_smaller_element_to_left(nums) -> list:
#     pass
#
#
# def sanitize_input_for_better_calculations(nums):
#     # For making calculations correct for case of NSR
#     # Adding a value at end, so instead of putting -1 for the original last element,
#     # we can put, our new fake last element's index
#
#     nums.append(0)  # A building with 0 height
#     # no need to put on left side, as its before 0'th index, so it will get -1 as index only
#
#     # Notice : modifying the original array her
#
#
# def mah(nums) -> int:  # Return Max Area
#     sanitize_input_for_better_calculations(nums)  # modifying the actual array
#     print("sanitized : ", nums)
#
#     nsr_index = indexes_of_next_smaller_element_to_right(nums)
#     nsl_index = indexes_of_next_smaller_element_to_left(nums)
#     print(nsr_index)
#     pass
#
#
# if __name__ == '__main__':
#     buildings = list(map(int, input().strip().split()))
#     print(mah(buildings))
#
# """
# 6 2 5 4 5 1 6
# """
