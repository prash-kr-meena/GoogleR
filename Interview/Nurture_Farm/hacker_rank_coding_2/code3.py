# Was getting TLE so memoized

# Note : Finally Accepted

# memoize pair of i,j as the key
memoize_downward = {}


def find_max_in_downward_direction(board, i, j) -> int:
    rows = len(board)
    columns = len(board[0])

    # If out of bound
    if i < 0 or i >= rows:
        return 0
    if j < 0 or j >= columns:
        return 0

    # if memoized, return result
    if memoize_downward.get((i, j)) is not None:
        return memoize_downward.get((i, j))

    # 3 options to choose from, choose all of them and revert them as well
    maximum_sum = 0
    maximum_sum += board[i][j]

    # Option 1
    sum_by_choosing_bottom_left_cell = find_max_in_downward_direction(board, i + 1, j - 1)

    # Option 2
    sum_by_choosing_bottom_cell = find_max_in_downward_direction(board, i + 1, j)

    # Option 3
    sum_by_choosing_bottom_right_cell = find_max_in_downward_direction(board, i + 1, j + 1)

    maximum_sum = maximum_sum + max(sum_by_choosing_bottom_left_cell,
                                    sum_by_choosing_bottom_cell,
                                    sum_by_choosing_bottom_right_cell)

    memoize_downward[(i, j)] = maximum_sum
    return maximum_sum


# ==========================================================================================

# memoize pair of i,j as the key
memoize_upward = {}


def find_max_in_upward_direction(board, i, j) -> int:
    rows = len(board)
    columns = len(board[0])

    # If out of bound
    if i < 0 or i >= rows:
        return 0
    if j < 0 or j >= columns:
        return 0

    # if memoized, return result
    if memoize_upward.get((i, j)) is not None:
        return memoize_upward.get((i, j))

    # 3 options to choose from, choose all of them and revert them as well
    maximum_sum = 0
    maximum_sum += board[i][j]

    # Option 1
    sum_by_choosing_upper_left_cell = find_max_in_upward_direction(board, i - 1, j - 1)

    # Option 2
    sum_by_choosing_upper_cell = find_max_in_upward_direction(board, i - 1, j)

    # Option 3
    sum_by_choosing_upper_right_cell = find_max_in_upward_direction(board, i - 1, j + 1)

    maximum_sum = maximum_sum + max(sum_by_choosing_upper_left_cell,
                                    sum_by_choosing_upper_cell,
                                    sum_by_choosing_upper_right_cell)

    memoize_upward[(i, j)] = maximum_sum
    return maximum_sum


def maxPathSum(board, p, q):
    row_count = len(board)
    down_max = find_max_in_downward_direction(board, 0, p)
    up_max = find_max_in_upward_direction(board, row_count - 1, q)

    maximum_sum_found = max(down_max, up_max)
    # print(maximum_sum_found)
    return maximum_sum_found


"""
3
3
9 4 7
2 1 3
1 4 2
2
1
"""

"""
STDIN      Function
-----      --------
3        → board[] size n = 3 (rows)  
3        → board[][] size m = 3 (columns)
9 4 7    → board = [[9, 4, 7], [2, 1, 3], [1, 4, 2]]
2 1 3
1 4 2
2        → p = 2
1        → 1 = 1


3
3
9 4 7 
2 1 3
1 4 2
2
1


"""
