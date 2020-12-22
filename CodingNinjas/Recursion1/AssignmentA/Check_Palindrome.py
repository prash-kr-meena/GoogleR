from sys import setrecursionlimit

from Utils.Boolean import print_small_boolean


def is_palindrome_i(string):
    i, j = 0, len(string) - 1
    is_palindrome = True

    while i < j:
        if string[i] != string[j]:
            is_palindrome = False
            break
        i += 1
        j -= 1

    return is_palindrome


# ------------------------------
# Index based implementation

def is_palindrome(string, left, right):
    # Base Case
    if left >= right:
        return True

    # Induction
    if string[left] != string[right]:
        return False
    else:
        # Hypothesis
        return is_palindrome(string, left + 1, right - 1)


def is_palindrome_r(string):
    return is_palindrome(string, 0, len(string) - 1)


if __name__ == '__main__':
    setrecursionlimit(11000)
    # test_string = "racecar"
    # test_string = "ninja"
    test_string = input()
    print_small_boolean(is_palindrome_i(test_string))
    print_small_boolean(is_palindrome_r(test_string))
