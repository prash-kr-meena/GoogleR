# InterviewBit Question
# https://www.interviewbit.com/problems/generate-all-parentheses-ii/

# This time our inputs are available_open_brackets and available_close_brackets
def balanced(parentheses):
    score = 0  # +1 for open and -1 for close

    for char in parentheses:
        if char == '(':
            score += 1
        else:
            score -= 1

        if score < 0:
            return False

    return True if score == 0 else False
    # Score 0, means the string was balanced


def get_balanced_parentheses(available_open_brackets, available_close_brackets, all_balanced_parentheses, output):
    if available_open_brackets == 0 and available_close_brackets == 0:
        # You can directly check here, for the output, if it is balanced or not, BEFORE printing it -> O(n * 2^n)
        # Or you can store them and later on check if balanced or not
        if balanced(output):
            all_balanced_parentheses.append(output)
        return

    if available_open_brackets != 0:
        output_when_using_open_bracket = output + "("
        get_balanced_parentheses(available_open_brackets - 1, available_close_brackets,
                                 all_balanced_parentheses, output_when_using_open_bracket)

    if available_close_brackets != 0:
        output_when_using_closed_bracket = output + ")"
        get_balanced_parentheses(available_open_brackets, available_close_brackets - 1,
                                 all_balanced_parentheses, output_when_using_closed_bracket)


class Solution:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, n):
        available_open_brackets = n
        available_close_brackets = n
        all_balanced_parentheses = []
        get_balanced_parentheses(available_open_brackets, available_close_brackets, all_balanced_parentheses, "")
        return all_balanced_parentheses


if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(0))
    print(s.generateParenthesis(1))
    print(s.generateParenthesis(2))
    print(s.generateParenthesis(3))
    print(s.generateParenthesis(4))
