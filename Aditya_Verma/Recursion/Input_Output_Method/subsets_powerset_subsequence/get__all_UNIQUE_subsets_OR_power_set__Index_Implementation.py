# Note : Index base implementation
# Here for shortening the input size, we use index

# This can work with both string and substring
# String will automatically be converted into list_of_char
def get_unique_subsets(input: list, output: str, unique_subsets: set, index: int) -> None:
    if index >= len(input):
        unique_subsets.add(output)  # Note : Ankh band kar ke add, as it will handle duplicity automatically
        return

    output_when_chosen = output  # same as the parent Recursive Nodes output
    output_when_did_not_choose = output + str(input[index])

    get_unique_subsets(input, output_when_chosen, unique_subsets, index + 1)
    get_unique_subsets(input, output_when_did_not_choose, unique_subsets, index + 1)


def get_all_unique_subsets(data) -> set:
    unique_subsets = set()
    get_unique_subsets(data, "", unique_subsets, 0)  # Choosing Output to be Empty String  NOTE
    return unique_subsets


if __name__ == "__main__":
    # data = [1, 2, 3]  # a list
    # data = "abc"  # a string
    data = "aab"  # a string - having duplicates - Note : It Handles duplicates
    print(get_all_unique_subsets(data))
