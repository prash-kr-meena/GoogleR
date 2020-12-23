# n is the input
# but ones and zeros are here to support the logic for branching
# ones -> no_of_ones_used__to__make_the_whole_num
# zeros -> no_of_zeros_used__to__make_the_whole_num


def N_Bit_binary(n, ones=0, zeros=0, output="") -> None:
    if n == 0:
        print(output, end=" ")
        return

    # we can choose 1 every time
    output_when_choose_1 = output + "1"
    N_Bit_binary(n - 1, ones + 1, zeros, output_when_choose_1)

    if ones > zeros:
        # then we can choose to put 0 as well
        output_when_choose_0 = output + "0"
        N_Bit_binary(n - 1, ones, zeros + 1, output_when_choose_0)


def Generate_and_print_N_bit_binary(n):
    N_Bit_binary(n)
    print()


if __name__ == "__main__":
    Generate_and_print_N_bit_binary(1)
    Generate_and_print_N_bit_binary(2)
    Generate_and_print_N_bit_binary(3)
    Generate_and_print_N_bit_binary(4)
    Generate_and_print_N_bit_binary(5)
    Generate_and_print_N_bit_binary(6)
