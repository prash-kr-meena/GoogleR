"""
You have given N Gamers login and logout time.
Find the maximum logged in users at any instance of time.
Example: u1 => 1 6, u2 => 3 5, u3=> 2 3
Maximum number of users: 3 (at t = 3)

"""
"""
This problem is similar to the Minimum_Number_of_Platforms problem
"""

"""
    1    2    3    4    5    6
    u1 --------------------->u1
              u2------->u2
        u3--->u3
"""


def find_max_user(pair_list, n, min_login_time, max_logout_time):
    # print(pair_list, n, min_login_time, max_logout_time)

    prefix_time_arr = [0] * (max_logout_time + 2)
    for pair in pair_list:
        prefix_time_arr[pair[0]] += 1
        prefix_time_arr[pair[1] + 1] -= 1

    # print(prefix_time_arr)

    # doing prefix sum
    for i in range(1, len(prefix_time_arr)):
        prefix_time_arr[i] += prefix_time_arr[i - 1]

    # print(prefix_time_arr)
    max_no_of_user = max(prefix_time_arr)
    # print(max_no_of_user)
    return max_no_of_user


if __name__ == '__main__':
    n = int(input())

    pair_list = []
    min_login_time = float("inf")
    max_logout_time = float("-inf")

    for i in range(n):
        # Assumption : pair[0] = login,  pair[0]1] = logout,
        pair = tuple(map(int, input().strip().split()))
        min_login_time = min(pair[0], min_login_time)
        max_logout_time = max(pair[1], max_logout_time)
        pair_list.append(pair)

    find_max_user(pair_list, n, min_login_time, max_logout_time)

"""
3
1 6
3 5
2 3


3
1 6
1 2 
3 4
"""
# [1,6] [3,5] [2,3]

# [1, 6] [1, 2] [3, 4]

# login : 1
#  2 3 4 5
# logut : 6

# [  * * * * * ]


# [1,6] [3,5] [2,3]
# 1 6
# [0 | 0 0 0 0 0 0 | 0]
# [0 | 1 0 0 0 0 0 | -1]
# [0 | 1 0 1 0 0 -1 | -1]
# [0 | 1 1 0 -1 0 0 | -1]
# [0 | 1 2 2 1 1 1 | 0]

# [0 1 1 1 -1 0 -1 -1]
# [0 1 2 3 2 2 1 1 0]

# [1, 6] [1, 2] [3, 4]
# [0 | 1 0 0 0 0 0 | -1]
# [0 | 2 0 -1 0 0 0 | -1]
# [0 | 2 0 0 -1 0 0 | -1]
# [0 | 2 2 2 1 1 1 | 0]
