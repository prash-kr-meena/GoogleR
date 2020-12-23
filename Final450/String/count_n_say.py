class Solution:

    def countAndSay__iterative(self, n: int) -> str:
        if n <= 0: return ""  # EMPTY
        if n == 1: return "1"

        say_prev = "1"
        for i in range(2, n + 1):  # n included
            say_curr = self.convert(say_prev)
            say_prev = say_curr

        return say_prev

    # Recursion1 tree is skewed, takes O(n) time for recursion, where n is the number
    # for each recursion it convert part, which is O(string_len),   and string_len in worst case would be n
    # So total Time : O(n2)

    # Takes O(n) space due to recursion,   as solving for n, n-1, n-2 ..... n=1
    # and at each level, we will be having a string to create which will keep on increase with n,
    # this string is data is destroyed as well after that perticular method
    # so space : (n + str_len)
    # interesting is how this str_len grows
    def countAndSay__recursive(self, n: int) -> str:
        if n <= 0: return ""  # EMPTY
        if n == 1: return "1"

        prev_say = self.countAndSay__recursive(n - 1)

        # convert into different_string
        my_say = self.convert(prev_say)
        return my_say

    # Time  : O(string_len)
    # Space : O(string_size)    at each recursion level it is, being created and destroyed
    @staticmethod
    def convert(say):
        characters = []

        prev_char = say[0]
        count = 0
        for curr_char in say:
            if prev_char != curr_char:
                characters.append(str(count))
                characters.append(prev_char)
                prev_char = curr_char
                count = 1
            else:
                count += 1

        # handle last element
        characters.append(str(count))
        characters.append(prev_char)

        return ''.join(characters)


if __name__ == "__main__":
    sol = Solution()

    for i in range(10):
        print(sol.countAndSay__recursive(i))

    for i in range(10):
        print(sol.countAndSay__iterative(i))

    # print(sol.convert("111221"))
