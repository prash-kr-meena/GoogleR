# here input is available_open_brackets and available_close_brackets
def generate_balanced_parentheses(available_open_brackets, available_close_brackets, output):
    if available_open_brackets == 0 and available_close_brackets == 0:
        print(output, end=" ")
        return

    # We always have one choice, of choosing the open bracket - To balance them
    if available_open_brackets != 0:
        output_when_using_open_bracket = output + "("
        generate_balanced_parentheses(available_open_brackets - 1, available_close_brackets,
                                      output_when_using_open_bracket)

    # But we only have the option of choosing the closed bracket when we have more closed bracket - To balance them

    if available_open_brackets < available_close_brackets:
        if available_close_brackets != 0:
            output_when_using_closed_bracket = output + ")"
            generate_balanced_parentheses(available_open_brackets, available_close_brackets - 1,
                                          output_when_using_closed_bracket)


def directly_generate_balanced_parentheses(n):
    available_open_brackets = n
    available_close_brackets = n
    output = ""
    generate_balanced_parentheses(available_open_brackets, available_close_brackets, output)
    print()


if __name__ == "__main__":
    directly_generate_balanced_parentheses(1)
    directly_generate_balanced_parentheses(2)
    directly_generate_balanced_parentheses(3)
    directly_generate_balanced_parentheses(4)
    directly_generate_balanced_parentheses(5)
