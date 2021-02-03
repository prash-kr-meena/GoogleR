def is_rotation_of_one_another__constant_space(A, B) -> bool:
    if len(A) != len(B):
        return False  # can't possibly be rotation of each other

    # checking if B is rotation of A
    firt_char_of_B = B[0]

    # index_of_it_in_A = A.find(firt_char_of_B)     # WILL Not be able to handle duplicity, as only returns first index

    """
    NOT implementing a little complex - Can be done easily with other methods
    
    1. for the case when There is not duplicate character
        -> You will get on index in A
        -> Now go through all the characters of B and A simultaneously and check character by character
        -> Note : In case of A, you probably need to get the mod or use some other way to cycle back to index 0 
        -> and in final if no mismatch found, The answer is true 
        
    2. For duplicate characters in the string
        -> You will get more then one indices in A, so store them in a list
        -> for all of the above index 
            -> Now go through all the characters of B and A simultaneously and check character by character
            -> Note : In case of A, you probably need to get the mod or use some other way to cycle back to index 0 
            -> If found any mismatch, then break the inside loop and start checking for the above variables 
            -> and in final if no mismatch found, Then   
            
    
    Consider a case like this
    A = "AAAAB"
    B = "ABAAA"
    
    here for the initial 3 A, the comparison is not fruitful
            
    Benefit of this is, its Constant space and
    could take less time in some cases
    """


def is_rotation_of_one_another__substring_way(A, B):
    if len(A) != len(B):
        return False  # can't possibly be rotation of each other

    big_string = A + A
    return big_string.find(B) >= 0  # if found - result in a non -ve number


"""
For better space and time complexity you can use KMP - Matchers

"""

if __name__ == "__main__":
    str_A = "ABCDE"  # str_A & str_B are same
    str_B = "ABCDE"
    print(is_rotation_of_one_another__substring_way(str_A, str_B))
    print(is_rotation_of_one_another__constant_space(str_A, str_B))  # Not implemented

"""
str_A = "ABAC"         # case with duplicity -- Important Case
str_B = "ACAB"

str_A = "ABAC"         # Not presents
str_B = "XXXX"

str_A = "ABCDE"          # str_A & str_B are same
str_B = "ABCDE"

str_A = "ABCDE"
str_B = "BCDEA"

str_A = "ABCDE"
str_B = "DEABC"
 
"""
