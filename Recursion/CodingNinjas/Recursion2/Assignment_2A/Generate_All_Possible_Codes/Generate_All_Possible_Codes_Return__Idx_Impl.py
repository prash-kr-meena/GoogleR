from sys import setrecursionlimit
from typing import List

from Utils.Array import print_array_multiline


def get_mapping(num: int) -> str:
    start_ordinal = ord('a') - 1  # 'a' -> 97, so we start from 96          This is because we are having 1 indexing
    return chr(start_ordinal + num)  # so when num is 1 -> 'a'  and 3 -> 'c'


"""
Doing index implementation : 

Well in this problem, both forward and backward Index-implementation would work, 
it is independent of that, ask why?

Well because we just need to replace the number with the correct mapping, so it doesn't matter from where we 
start the mapping from, we just need to maintain the final order and it will work fine

Pay focus on the Input-Output Diagram
"""


def all_codes(all_possible_codes, input, output, index) -> None:
    # Base Case
    if index >= len(input):
        all_possible_codes.append(output)
        return

    if index <= len(input) - 2:  # input_size >= 2:
        # Choose Single Digit
        single_digit = int(input[index])
        output_when_using_single_digit = output + get_mapping(single_digit)
        # input_when_using_single_digit = Changed through index, by increment of 1
        all_codes(all_possible_codes, input, output_when_using_single_digit, index + 1)

        # Choose Double Digits - If in range
        double_digit = int(input[index:index + 2])
        if 1 <= double_digit <= 26:
            output_when_using_double_digit = output + get_mapping(double_digit)
            # input_when_using_double_digit = Changed through index, by increment of 2 Notice
            all_codes(all_possible_codes, input, output_when_using_double_digit, index + 2)

    else:  # input_size < 2:
        # Choose Single Digit
        single_digit = int(input[index])
        output_when_using_single_digit = output + get_mapping(single_digit)
        # input_when_using_single_digit = Changed through index, by increment of 1
        all_codes(all_possible_codes, input, output_when_using_single_digit, index + 1)


def generate_all_possible_codes(number_string) -> List[str]:
    all_possible_codes = []
    all_codes(all_possible_codes, number_string, "", 0)
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
