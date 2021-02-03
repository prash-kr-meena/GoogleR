# This time our inputs are available_open_brackets and available_close_brackets
def generate_parentheses(available_open_brackets, available_close_brackets, output):
    if available_open_brackets == 0 and available_close_brackets == 0:
        print(output, end="  ")
        return

    if available_open_brackets != 0:
        output_when_using_open_bracket = output + "("
        generate_parentheses(available_open_brackets - 1, available_close_brackets, output_when_using_open_bracket)

    if available_close_brackets != 0:
        output_when_using_closed_bracket = output + ")"
        generate_parentheses(available_open_brackets, available_close_brackets - 1, output_when_using_closed_bracket)


def generate_all_parentheses(n):
    available_open_brackets = n
    available_close_brackets = n
    generate_parentheses(available_open_brackets, available_close_brackets, "")
    print()


if __name__ == "__main__":
    generate_all_parentheses(0)
    generate_all_parentheses(1)
    generate_all_parentheses(2)
    generate_all_parentheses(3)
