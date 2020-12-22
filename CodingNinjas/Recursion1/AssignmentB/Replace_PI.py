from sys import setrecursionlimit


# backward implementation
def replace_pi(string, n) -> str:
    if n == 0:
        return ""  # for string of length 0

    # so that we don't have to put a index check as we are indexing 2nd element
    if n == 1:
        return string[n - 1]  # only one element, return the last one
        # as this single element will not form pi

    # Hypothesis
    if string[n - 1] == 'i' and string[n - 2] == 'p':
        result_from_smaller_string = replace_pi(string, n - 2)  # shortening by 2 character
        return result_from_smaller_string + "3.14"  # Induction
    else:
        result_from_smaller_string = replace_pi(string, n - 1)  # shortening by 1 character
        return result_from_smaller_string + string[n - 1]  # Induction ->  adding the last character as it is


def replace_pi_r(string):
    if string is None:
        return string

    return replace_pi(string, len(string))


if __name__ == '__main__':
    setrecursionlimit(11000)
    input_string = input()
    print(replace_pi_r(input_string))
