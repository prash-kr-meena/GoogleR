from sys import setrecursionlimit

'''
Designed base case using the constraints, as it give the extreme values

1 <= x <= 30
0 <= n <= 30


Time  : O(n) as only one recursive call
Space : O(n) due to recursive call stack
'''


def power(x, n):
    if n == 0:
        return 1
    # if x == 1:		# Not needed, as we are not decreasing x
    #     return 1a

    return x * power(x, n - 1)  # induction step & Hypothesis Step


# Main
if __name__ == "__main__":
    setrecursionlimit(11000)
    x, n = list(int(i) for i in input().strip().split(' '))
    print(power(x, n))
