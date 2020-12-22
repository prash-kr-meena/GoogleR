# This time our inputs are available_open_brackets and available_close_brackets
def balanced(parentheses):
    score = 0  # +1 for open and -1 for close

    for char in parentheses:
        if char == '(':
            score += 1
        else:
            score -= 1

        if score < 0:
            return False

    return True if score == 0 else False
    # Score 0, means the string was balanced


def generate_parentheses(available_open_brackets, available_close_brackets, output):
    if available_open_brackets == 0 and available_close_brackets == 0:
        # You can directly check here, for the output, if it is balanced or not, BEFORE printing it -> O(n * 2^n)
        # Or you can store them and later on check if balanced or not
        if balanced(output):
            print(output, end=" ")
        return

    if available_open_brackets != 0:
        output_when_using_open_bracket = output + "("
        generate_parentheses(available_open_brackets - 1, available_close_brackets, output_when_using_open_bracket)

    if available_close_brackets != 0:
        output_when_using_closed_bracket = output + ")"
        generate_parentheses(available_open_brackets, available_close_brackets - 1, output_when_using_closed_bracket)


def generate_all_balanced_parentheses(n):
    available_open_brackets = n
    available_close_brackets = n
    generate_parentheses(available_open_brackets, available_close_brackets, "")
    print()


if __name__ == "__main__":
    generate_all_balanced_parentheses(1)
    generate_all_balanced_parentheses(2)
    generate_all_balanced_parentheses(3)
