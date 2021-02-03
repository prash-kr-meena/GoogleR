# Note : len base implementation
# Here for shortening the input size, we use index
# This can work with both string and substring


# Input can be list or string --> as operation will be same for both
def print_subsets(input, output: str) -> None:
    if len(input) == 0:
        print('"' + output + '"')
        return

    output_when_chosen = output  # same as the parent Recursive Nodes output
    output_when_did_not_choose = output + str(input[0])
    shorter_input = input[1:]  # substring from 1st character
    # For list, spaces are preferred in output, while for string space in the middle is not preferred  << Notice

    print_subsets(shorter_input, output_when_chosen)
    print_subsets(shorter_input, output_when_did_not_choose)


def print_all_string_subsets(data):
    print_subsets(data, "")  # Choosing Output to be Empty String


if __name__ == "__main__":
    data = [1, 2, 3]  # a list
    # data = [15, 20, 12]  # a list --> it works the the results, do not have the elements separated Notice, it's output

    # data = "abc"  # a string
    # data = "aab"  # a string -- having duplicates - Note : code is not designed to handle

    print_all_string_subsets(data)
