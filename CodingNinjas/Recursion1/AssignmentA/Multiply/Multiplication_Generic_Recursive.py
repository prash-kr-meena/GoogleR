from sys import setrecursionlimit


#   m + m + m + . . .  + m         n Times
def multiply(m, n) -> int:
    # Base Case
    if m == 0:
        return 0  # adding 0 n time will still result in 0

    if n == 0:
        return 0  # adding m (any number)  0 times will result in 0 only

    if n > 0:
        small_ans = multiply(m, n - 1)
        return small_ans + m
    else:
        small_ans = multiply(m, n + 1)
        return small_ans - m


if __name__ == '__main__':
    setrecursionlimit(11000)
    m = int(input())
    n = int(input())
    print(multiply(m, n))

"""
+ve +ve
    2
    3
    
+ve -ve
    2
    -5
    
-ve +ve
    -4
    2
    
-ve -ve
    -4
    -5
"""
