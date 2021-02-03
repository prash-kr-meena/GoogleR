def count_digits__iterative(number) -> int:
    count = 0
    while number >= 1:
        number //= 10  # number = number // 10
        count += 1

    return count


def count_digits__recursive(number) -> int:
    # Base Cases
    if number == 0:
        return 0  # 0 is not valid, Check the constraints

    if number <= 9:
        return 1

    # induction + hypothesis
    return 1 + count_digits__recursive(number // 10)


if __name__ == "__main__":
    number = int(input())
    print(count_digits__iterative(number))
    print(count_digits__recursive(number))

""" Test Cases

0123        # 3 not 4
0000001     # 1
1000        # 4
"""
