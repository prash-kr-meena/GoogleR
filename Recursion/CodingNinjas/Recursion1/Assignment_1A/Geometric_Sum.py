from sys import setrecursionlimit


def geometric_sum(k) -> float:
    # Base case
    if k == 0:
        return 1  # as 1/(2^0)

    # Hypothesis
    geometric_sum_till___k_minus_1 = geometric_sum(k - 1)

    # Induction
    return geometric_sum_till___k_minus_1 + 1 / (2 ** k)


if __name__ == '__main__':
    setrecursionlimit(11000)
    K = int(input())
    print("%.5f" % geometric_sum(K))
