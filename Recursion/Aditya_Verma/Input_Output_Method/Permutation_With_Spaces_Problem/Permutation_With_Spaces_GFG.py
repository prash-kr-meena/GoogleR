def print_space_separated_permutations(input, output="", index=0) -> None:
    # Base case
    if index >= len(input):
        print("(" + output + ")", end="")
        return

    # initially we only have one choice
    if index == 0:
        updated_output = input[index]
        print_space_separated_permutations(input, updated_output, index + 1)  # shortening input using index
    else:
        output_when_including_character_with_space = output + " " + input[index]
        output_when_ONLY_including_character = output + input[index]
        print_space_separated_permutations(input, output_when_including_character_with_space, index + 1)
        print_space_separated_permutations(input, output_when_ONLY_including_character, index + 1)


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        string = input()
        print_space_separated_permutations(string)
        print()
