# Note : len base implementation
# Here for shortening the input size, we use index
# This can work with both string and substring


# Input can be list or string --> as operation will be same for both
def get_unique_subsets(input, output: str, unique_subsets: set) -> None:
    if len(input) == 0:
        unique_subsets.add(output)
        return

    output_when_chosen = output  # same as the parent Recursive Nodes output
    output_when_did_not_choose = output + str(input[0])
    shorter_input = input[1:]  # substring from 1st character

    get_unique_subsets(shorter_input, output_when_chosen, unique_subsets)
    get_unique_subsets(shorter_input, output_when_did_not_choose, unique_subsets)


def get_all_unique_subsets(data):
    unique_subsets = set()
    get_unique_subsets(data, "", unique_subsets)  # Choosing Output to be Empty String
    return unique_subsets


if __name__ == "__main__":
    # data = [1, 2, 3]  # a list
    data = "abc"  # a string
    # data = "aab"  # a string -- having duplicates - Note : code is not designed to handle
    print(get_all_unique_subsets(data))
