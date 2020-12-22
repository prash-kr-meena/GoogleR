from sys import setrecursionlimit


def remove_consecutive_duplicates(string, n) -> str:
    # Base Case
    # for length 0 or 1 : there will be no question consecutive duplicates
    if n == 0:
        return ""

    if n == 1:
        return string[n - 1]  # return the last character

    # Hypothesis
    duplicates_removed_str = remove_consecutive_duplicates(string, n - 1)

    # Induction
    last_char_of_original_string = string[n - 1]
    last_char_of_result_string = duplicates_removed_str[-1]  # NOTE
    if last_char_of_original_string == last_char_of_result_string:
        return duplicates_removed_str
    else:
        return duplicates_removed_str + last_char_of_original_string


def remove_consecutive_duplicates_r(string) -> str:
    return remove_consecutive_duplicates(string, len(string))


if __name__ == '__main__':
    setrecursionlimit(11000)
    input_string = input().strip()
    print(remove_consecutive_duplicates_r(input_string))
