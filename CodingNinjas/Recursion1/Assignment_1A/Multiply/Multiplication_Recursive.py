from sys import setrecursionlimit


#   m + m + m + . . .  + m         n Times
def multiply(m, n) -> int:
    # Base Case
    if m == 0:
        return 0  # adding 0 n time will still result in 0

    if n == 0:
        return 0  # adding m (any number)  0 times will result in 0 only

    # Hypothesis
    m_multiplied_by__n_minus_1 = multiply(m, n - 1)

    # Induction
    return m_multiplied_by__n_minus_1 + m


if __name__ == '__main__':
    setrecursionlimit(11000)
    m = int(input())
    n = int(input())
    print(multiply(m, n))
