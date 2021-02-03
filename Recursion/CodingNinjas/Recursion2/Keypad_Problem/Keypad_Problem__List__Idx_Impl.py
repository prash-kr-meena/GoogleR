from sys import setrecursionlimit


# Index based Implementation << Note
# Here only printing, for storing we can pass a list and in the base case, append the output string into that list
def print_keypad_combinations(combinations, keypad, output, index) -> None:
    if index >= len(keypad):
        combinations.append(output)
        return

    keypad_chars = get_keypad_chars(keypad[index])
    for char in keypad_chars:
        updated_output = output + char
        print_keypad_combinations(combinations, keypad, updated_output, index + 1)


def get_keypad_chars(num: int) -> str:
    num = int(num)
    keypad_chars = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    return keypad_chars[num]


def get_all_possible_keypad_character_combination(keypad) -> list:
    combinations = []  # Just added this Notice
    print_keypad_combinations(combinations, keypad, "", 0)
    return combinations


if __name__ == '__main__':
    setrecursionlimit(11000)
    keypad_nums = input()  # Guaranteed to be integers
    print(get_all_possible_keypad_character_combination(keypad_nums))
