# Doing Index Implementation
def remove_x(string, n) -> str:
    if n == 0:
        return ""

    # Hypothesis
    result_from_smaller_str = remove_x(string, n - 1)

    # Induction
    # - checking the last character and taking decision over that
    last_char = string[n - 1]
    if last_char == 'x':
        return result_from_smaller_str
    else:
        return result_from_smaller_str + last_char


# Problem: Remove x from string - Recursively
def remove_x__r(string):
    if string is None:
        return None

    return remove_x(string, len(string))


if __name__ == '__main__':
    string = input()
    print(remove_x__r(string))
