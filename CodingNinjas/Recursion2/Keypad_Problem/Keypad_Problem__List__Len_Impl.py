from sys import setrecursionlimit


# Length based Implementation << Note
# Here only printing, for storing we can pass a list and in the base case, append the output string into that list
def print_keypad_combinations(combinations, keypad, output) -> None:
    if len(keypad) == 0:
        combinations.append(output)
        return

    keypad_chars = get_keypad_chars(keypad[0])  # Always get keypad_chars for first number, as we gonna remove it
    for char in keypad_chars:
        updated_output = output + char
        updated_keypad = keypad[1:]  # substring, removing the first char
        print_keypad_combinations(combinations, updated_keypad, updated_output)


def get_keypad_chars(num: int) -> str:
    num = int(num)
    keypad_chars = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    return keypad_chars[num]


def print_all_possible_keypad_character_combination(keypad) -> list:
    combinations = []  # Just added this Notice
    print_keypad_combinations(combinations, keypad, "")
    return combinations


if __name__ == '__main__':
    setrecursionlimit(11000)
    keypad_nums = input()  # Guaranteed to be integers
    print(print_all_possible_keypad_character_combination(keypad_nums))
