from sys import setrecursionlimit


#  Index based Implementation << Note
# Here only printing, for storing we can pass a list and in the base case, append the output string into that list
def print_keypad_combinations(keypad, output, index) -> None:
    if index >= len(keypad):
        print(output)
        return

    keypad_chars = get_keypad_chars(keypad[index])
    for char in keypad_chars:
        updated_output = output + char
        print_keypad_combinations(keypad, updated_output, index + 1)


def get_keypad_chars(num: int) -> str:
    num = int(num)
    keypad_chars = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    return keypad_chars[num]


def print_all_possible_keypad_character_combination(keypad) -> None:
    print_keypad_combinations(keypad, "", 0)


if __name__ == '__main__':
    setrecursionlimit(11000)
    keypad_nums = input()  # Guaranteed to be integers
    print_all_possible_keypad_character_combination(keypad_nums)
