from sys import setrecursionlimit


def convert_char_into_int(char: str) -> int:
    # # Assumed the characters represents a number
    return ord(char) - ord('0')


def str_to_int(num_string: str, n: int) -> int:
    # Assuming it will never be 0
    if n == 1:
        last_char = num_string[n - 1]
        return convert_char_into_int(last_char)

    # Hypothesis
    integer_from_smaller_str = str_to_int(num_string, n - 1)

    # Induction
    last_char = num_string[n - 1]
    last_digit = convert_char_into_int(last_char)
    return integer_from_smaller_str * 10 + last_digit


# Lets do a len implementation of it
def remove_leading_zeros(num_string: str) -> str:
    # Base Case
    if len(num_string) == 0:
        return num_string  # or return ""

    # Hypothesis - Making Input smaller
    first_char = num_string[0]
    if first_char == '0':
        return remove_leading_zeros(num_string[1:])
    else:
        return num_string  # Induction


def str_to_int__recursive(num_string: str) -> int:
    # assumed the len of numeric_string will not be 0
    num_string_without_leading_zeros = remove_leading_zeros(num_string)
    # print(num_string_without_leading_zeros, "<<<")
    if len(num_string_without_leading_zeros) == 0:
        num_string_without_leading_zeros = '0'  # for cases when string was 000000

    return str_to_int(num_string_without_leading_zeros, len(num_string_without_leading_zeros))


#  Here, it is guaranteed that the characters are integers only Note <<
if __name__ == '__main__':
    setrecursionlimit(11000)
    numeric_string = input()
    result = str_to_int__recursive(numeric_string)
    print(result)
    print(type(result))
