from Tree.CodingNinjas.GenericTree.GenericTree import GenericTree
from Utils.Array import input_array
from Utils.Boolean import print_lowercase_boolean

"""
Given a generic tree and an integer x, check if x is present in the given tree or not. 
Return true if x is present, return false otherwise.

successfully submitted,
Note : in the tests the variable is not on another line, but in the same line as first element
"""


def check_if_tree_contains_x(root, x) -> bool:
    if root is None:
        return False

    if root.data == x:  # if at root then return, else check for children
        return True

    for child in root.children:
        exists = check_if_tree_contains_x(child, x)
        if exists:  # else keep checking in other children
            return True

    return False  # if not yet found


if __name__ == '__main__':
    x = int(input())
    array = input_array("")
    tree_root = GenericTree.single_line_input(array)
    found = check_if_tree_contains_x(tree_root, x)
    print_lowercase_boolean(found)
"""
40
10 3 20 30 40 2 40 50 0 0 0 0 
True << Output

4
10 3 20 30 40 2 40 50 0 0 0 0 
False << Output
"""
