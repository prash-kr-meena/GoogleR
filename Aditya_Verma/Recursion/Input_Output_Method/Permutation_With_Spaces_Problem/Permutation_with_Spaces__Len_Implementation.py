# We have default arguments
def print_permutation_with_spaces(input, output) -> None:
    if len(input) == 0:
        print(output)
        return

    output_when_including_character_with_space = output + " " + input[0]
    output_when_ONLY_including_character = output + input[0]
    updated_input = input[1:]
    print_permutation_with_spaces(updated_input, output_when_including_character_with_space)
    print_permutation_with_spaces(updated_input, output_when_ONLY_including_character)


def print_permutation_with_spaces__len_implementation(input) -> None:
    output = input[0]  # First character of input, as we don't need to take decision for that
    updated_input = input[1:]
    print_permutation_with_spaces(updated_input, output)


if __name__ == "__main__":
    print_permutation_with_spaces__len_implementation("ABC")
