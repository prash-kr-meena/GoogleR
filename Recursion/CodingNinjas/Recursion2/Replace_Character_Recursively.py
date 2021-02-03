from sys import setrecursionlimit


def replace_chars(string, char_to_be_replaced, char_to_replace_with, n) -> str:
    if n == 0:
        return ""

    # Hypothesis
    result_from_smaller_str = replace_chars(string, char_to_be_replaced, char_to_replace_with, n - 1)

    # Induction
    last_char = string[n - 1]
    if last_char == char_to_be_replaced:
        return result_from_smaller_str + char_to_replace_with
    else:
        return result_from_smaller_str + last_char


def replace_chars_r(string, char_to_be_replaced, char_to_replace_with) -> str:
    return replace_chars(string, char_to_be_replaced, char_to_replace_with, len(string))


if __name__ == '__main__':
    setrecursionlimit(11000)
    text = input()
    char_replaced, char_replacing = input().strip().split(" ")
    result = replace_chars_r(text, char_replaced, char_replacing)
    print(result)
