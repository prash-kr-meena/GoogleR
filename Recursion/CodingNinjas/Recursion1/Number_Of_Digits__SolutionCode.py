from sys import getrecursionlimit
from sys import setrecursionlimit


def custom_recursion_limit():
    print("Default Recursion1 Limit : ", getrecursionlimit())
    setrecursionlimit(11000)
    print("Updated Recursion1 Limit : ", getrecursionlimit())


def count(num) -> int:
    if num == 0:
        return 0

    # Hypothesis
    answer_for_smaller_input = count(num // 10)

    # induction
    return 1 + answer_for_smaller_input


if __name__ == "__main__":
    custom_recursion_limit()
    n = int(input(">> "))
    print(count(n))
