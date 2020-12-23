# We have default arguments
def print_permutation_with_spaces(input, output="", index=0) -> None:
    # Base case
    if index >= len(input):
        print(output)
        return

    # initially we only have one choice
    if index == 0:
        updated_output = input[index]
        print_permutation_with_spaces(input, updated_output, index + 1)  # shortening input using index
    else:
        output_when_including_character_with_space = output + " " + input[index]
        output_when_ONLY_including_character = output + input[index]
        print_permutation_with_spaces(input, output_when_including_character_with_space, index + 1)
        print_permutation_with_spaces(input, output_when_ONLY_including_character, index + 1)


if __name__ == "__main__":
    print_permutation_with_spaces("ABC")  # default data will be set for other params
