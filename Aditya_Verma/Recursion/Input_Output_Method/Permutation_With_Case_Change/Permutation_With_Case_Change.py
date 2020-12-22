# Time : O(2^n)  ie, Exponential
def print_permutations_with_case_change(input: str, output="", index=0):
    if index >= len(input):
        print(output)
        return

    current_char = input[index]
    current_char_with_case_change = current_char.upper() if current_char.islower() else current_char.lower()
    output_without_case_change = output + current_char
    output_with_case_change = output + current_char_with_case_change
    # Will update, input through updating index

    print_permutations_with_case_change(input, output_without_case_change, index + 1)
    print_permutations_with_case_change(input, output_with_case_change, index + 1)

    pass


if __name__ == "__main__":
    print_permutations_with_case_change("ab")
