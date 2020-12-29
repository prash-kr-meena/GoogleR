from sys import setrecursionlimit
from typing import List

from Utils.Array import print_array_multiline


def get_mapping(num: int) -> str:
    start_ordinal = ord('a') - 1  # 'a' -> 97, so we start from 96          This is because we are having 1 indexing
    return chr(start_ordinal + num)  # so when num is 1 -> 'a'  and 3 -> 'c'


"""
Doing Length implementation
Pay focus on the Input-Output Diagram
"""


def all_codes(all_possible_codes, input, output) -> None:
    input_size = len(input)
    # Base Case
    if input_size == 0:
        all_possible_codes.append(output)
        return

    if input_size >= 2:
        # Choose Single Digit
        single_digit = int(input[0])
        output_when_using_single_digit = output + get_mapping(single_digit)
        input_when_using_single_digit = input[1:]  # substring with 1 element skipped
        all_codes(all_possible_codes, input_when_using_single_digit, output_when_using_single_digit)

        # Choose Double Digits - If in range
        double_digit = int(input[0:2])
        if 1 <= double_digit <= 26:
            output_when_using_double_digit = output + get_mapping(double_digit)
            input_when_using_double_digit = input[2:]  # substring with 1 element skipped
            all_codes(all_possible_codes, input_when_using_double_digit, output_when_using_double_digit)
    else:
        # Choose Single Digit
        single_digit = int(input[0])
        output_when_using_single_digit = output + get_mapping(single_digit)
        input_when_using_single_digit = input[1:]  # substring with 1 element skipped
        all_codes(all_possible_codes, input_when_using_single_digit, output_when_using_single_digit)


def generate_all_possible_codes(number_string) -> List[str]:
    all_possible_codes = []
    all_codes(all_possible_codes, number_string, "")
    return all_possible_codes


if __name__ == '__main__':
    setrecursionlimit(11000)
    num_str = input()
    codes = generate_all_possible_codes(num_str)
    print_array_multiline(codes)

"""
1123
9999
"""
