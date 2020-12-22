def pair_star(string, n) -> str:
    # Base case
    if n == 0:
        return ""  # Nothing to process

    # so that we don't have to put a index check as we are indexing 2nd element
    if n == 1:
        return string[n - 1]  # only one element, return the last one
        # as this single element will not form a pair

    # Hypothesis
    result_from_smaller_string = pair_star(string, n - 1)  # Note: as the 2ndLast character could form another pair

    # Induction
    last_char = string[n - 1]
    second_last_char = string[n - 2]
    if last_char == second_last_char:
        return result_from_smaller_string + "*" + last_char  # ->  adding * before this character
    else:
        return result_from_smaller_string + last_char  # ->  adding the last character as it is


def pair_star_r(string) -> str:
    return pair_star(string, len(string))


if __name__ == '__main__':
    input_str = input()
    print(pair_star_r(input_str))
