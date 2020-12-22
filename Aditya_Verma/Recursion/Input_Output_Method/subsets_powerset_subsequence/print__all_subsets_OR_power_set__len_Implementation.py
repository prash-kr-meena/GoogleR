# Note : len base implementation
# Here for shortening the input size, we use index
# This can work with both string and substring


# Input can be list or string --> as operation will be same for both
def print_subsets(input, output: str) -> None:
    if len(input) == 0:
        print("'", output, "'")
        return

    output_when_chosen = output  # same as the parent Recursive Nodes output
    output_when_did_not_choose = output + str(input[0])
    shorter_input = input[1:]  # substring from 1st character

    print_subsets(shorter_input, output_when_chosen)
    print_subsets(shorter_input, output_when_did_not_choose)


def print_all_subsets(data):
    print_subsets(data, "")  # Choosing Output to be Empty String


if __name__ == "__main__":
    data = [1, 2, 3]  # a list
    # data = "abc"  # a string
    # data = "aab"  # a string -- having duplicates - Note : code is not designed to handle
    print_all_subsets(data)
