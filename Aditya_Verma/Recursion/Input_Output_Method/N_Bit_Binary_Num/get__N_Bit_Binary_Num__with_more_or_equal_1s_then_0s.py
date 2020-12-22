# n is the input
# but ones and zeros are here to support the logic for branching
# ones -> no_of_ones_used__to__make_the_whole_num
# zeros -> no_of_zeros_used__to__make_the_whole_num
from typing import List


def N_Bit_binary(n, ones, zeros, output, n_bit_nums: List[str]) -> None:
    if n == 0:
        n_bit_nums.append(output)
        return

    # we can choose 1 every time
    output_when_choose_1 = output + "1"
    N_Bit_binary(n - 1, ones + 1, zeros, output_when_choose_1, n_bit_nums)

    if ones > zeros:
        # then we can choose to put 0 as well
        output_when_choose_0 = output + "0"
        N_Bit_binary(n - 1, ones, zeros + 1, output_when_choose_0, n_bit_nums)


def Generate_and_Return__N_bit_binary(n):
    n_bit_nums = []
    ones = 0
    zeros = 0
    output = ""
    N_Bit_binary(n, ones, zeros, output, n_bit_nums)
    return n_bit_nums


if __name__ == "__main__":
    print(Generate_and_Return__N_bit_binary(1))
    print(Generate_and_Return__N_bit_binary(2))
    print(Generate_and_Return__N_bit_binary(3))
    print(Generate_and_Return__N_bit_binary(4))
    print(Generate_and_Return__N_bit_binary(5))
    print(Generate_and_Return__N_bit_binary(6))
