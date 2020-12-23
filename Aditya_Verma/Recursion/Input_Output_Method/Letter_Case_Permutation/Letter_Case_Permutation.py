from typing import List


# Note : You can return the output in any order.
# in worst case, all characters are alphabets, hence 2 choices for each so its exponential
# Time : O(2^n)

def get_letter_case_permutations(permutations: List[str], input, output="", index=0):
    if index >= len(input):
        permutations.append(output)
        return

    current_char = input[index]
    if current_char.isdigit():
        # if the character is a digit we only have one choice
        updated_output = output + current_char
        get_letter_case_permutations(permutations, input, updated_output, index + 1)  # updated input,via index
    else:
        # if it is an alphabet, we have two choices
        current_char_with_case_change = current_char.upper() if current_char.islower() else current_char.lower()
        output_without_case_change = output + current_char
        output_with_case_change = output + current_char_with_case_change

        get_letter_case_permutations(permutations, input, output_without_case_change, index + 1)
        get_letter_case_permutations(permutations, input, output_with_case_change, index + 1)  # updated input,via index


class Solution:

    def letter_case_permutation(self, string: str) -> List[str]:
        all_permutations = []  # it will be, list of string
        get_letter_case_permutations(all_permutations, string)
        return all_permutations


if __name__ == "__main__":
    solution = Solution()
    print(solution.letter_case_permutation("a1b2"))
    print(solution.letter_case_permutation("3z4"))
    print(solution.letter_case_permutation("12345"))
    print(solution.letter_case_permutation("0"))
