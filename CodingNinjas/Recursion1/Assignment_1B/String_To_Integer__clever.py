from sys import setrecursionlimit


# NOTE : the clever part is just that, you don't need to remove the leading 0's
#        The math still works out well
# As it does not matter how many time you multiply 0 by 10 and add 0 to it, it will still result in 0

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


def str_to_int__recursive(num_string: str) -> int:
    # assumed the len of numeric_string will not be 0
    return str_to_int(num_string, len(num_string))


#  Here, it is guaranteed that the characters are integers only Note <<
if __name__ == '__main__':
    setrecursionlimit(11000)
    numeric_string = input()
    result = str_to_int__recursive(numeric_string)
    print(result)
    print(type(result))
