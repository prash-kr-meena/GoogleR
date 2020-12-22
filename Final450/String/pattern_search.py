# naive - bruteforce
# kmp
# KMP Algorithm

"""
"""


# Time : O(n2)
# Space : O(1)
def pattern_search_brute_force(text, pattern):
    for text_index, text_char in enumerate(text):
        if text_char == pattern[0]:  # matches to first character of pattern string

            # check remaining length in text
            remaining_chars_in_text = len(text) - text_index
            if len(pattern) > remaining_chars_in_text:  # can't possibly contain the pattern, continue
                continue

            is_matching = True  # by default true
            tmp_text_index = text_index  # to move forward in text string

            for pattern_index, pattern_char in enumerate(pattern):
                if pattern_char != text[tmp_text_index]:
                    is_matching = False
                    break
                tmp_text_index += 1  # move in text string

            if is_matching:
                print("found pattern {} at {}".format(pattern, text_index))


if __name__ == "__main__":
    text_str = "AABAACAADAABAAABAA"
    pattern_str = "AABA"
    pattern_search_brute_force(text_str, pattern_str)

"""
text_str = "AABAACAADAABAABA"
pattern_str = "AABA"


text_str = "AABAACAADAABAAABAA"
pattern_str = "AABA"

text_str = "AABCCAADDEE"
pattern_str = "FAA"




"""
