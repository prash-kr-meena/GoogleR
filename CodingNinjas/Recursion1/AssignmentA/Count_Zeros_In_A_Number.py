from sys import setrecursionlimit

"""
Here in actuality you should treat it as number

But the implementation could be made easy if we convert it in a string or list <By Traversing>

We will do both the implementations

"""


# taking numbers as input
# The question requrement does not ask to handle -ve numbers,
# But, we can handle by a simple check, where in we can convert the -ve num to a +ve number

def count_zeros(num: int) -> int:
    # Edge Case - Handling -ve num
    if num < 0:
        num = num * -1

    # Base Case
    if num == 0:
        return 1
    if 0 < num <= 9:
        return 0  # Important

    # Hypothesis
    updated_num, last_num = divmod(num, 10)
    zero_count_in_smaller_num = count_zeros(updated_num)

    # Induction
    if last_num == 0:
        return zero_count_in_smaller_num + 1
    else:
        return zero_count_in_smaller_num


# converting into an iterable string or list
def count_zeros_v2(string, n) -> int:
    if n == 0:
        return 0  # exhausted the search space

    # Hypothesis
    zero_count_in_smaller_num = count_zeros_v2(string, n - 1)

    # Induction
    last_element = string[n - 1]
    if last_element == '0':
        return zero_count_in_smaller_num + 1
    else:
        return zero_count_in_smaller_num


def count_zeros_iterable(num: int) -> int:
    string = str(num)
    return count_zeros_v2(string, len(string))


if __name__ == '__main__':
    setrecursionlimit(11000)
    number = int(input())
    print(count_zeros(number))
    print(count_zeros_iterable(number))
