# from sys import setrecursionlimit
#
# from Util.Boolean import print_small_boolean
#
# """
# Index based Implementation
# Here backward implementation doesn't make sense, because of the nature of the problem
# """
#
#
# def check_string_complies_with_rule(ab_string, index=0) -> bool:
#     pass
#
#
# # Length based Implementation
# def check_ab__len_impl(ab_string):
#     if len(ab_string) != 0 and ab_string[0] != 'a':
#         return False
#
#     return check_ab(ab_string[1:])  # excluding the 1st character
#
#
# def check_ab(ab_string):
#     # Edge Case
#     if len(ab_string) == 0:
#         return True  # No character present, follows the rule
#
#     # 3 options, 'a' , 'bb'  and Empty string (already covered in base case)
#     # Hypothesis
#     if ab_string[0] == 'a':
#         return check_ab(ab_string[1:])  # skipping first characters
#     elif len(ab_string) >= 2 and ab_string[0:3] == 'bb':
#         return check_ab(ab_string[2:])  # skipping first 2 characters
#     else:
#         return False
#
#
# if __name__ == '__main__':
#     setrecursionlimit(11000)
#     input_ab = input()
#     # print_small_boolean(check_string_complies_with_rule(input_ab))
#     print_small_boolean(check_ab__len_impl(input_ab))
