"""
Whole Code Written By Me
"""


def minimum_subset_sum_difference(nums, curr_index, A, B):
    if curr_index >= len(nums):  # base case
        # or abs(sum(A) - sum(B))       << One liner
        sum_A = sum(A)
        sum_B = sum(B)
        return abs(sum_A - sum_B)

    # include only in setA but not B
    A.append(nums[curr_index])
    min_diff_with_A = minimum_subset_sum_difference(nums, curr_index + 1, A, B)  # with A modified
    A.pop()  # undo

    # include only in setB but not A
    B.append(nums[curr_index])
    min_diff_with_B = minimum_subset_sum_difference(nums, curr_index + 1, A, B)  # with B modified
    B.pop()  # undo

    return min(min_diff_with_A, min_diff_with_B)


def solve(nums):
    if nums is None or len(nums) == 0:  # Edge case
        return float("inf")

    print(minimum_subset_sum_difference(nums, 0, [], []))


def main():
    solve([1, 2, 7, 1, 5])
    solve([1, 2, 3, 9])
    solve([1, 3, 100, 4])


main()
