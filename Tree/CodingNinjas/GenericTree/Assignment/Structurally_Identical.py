from Tree.CodingNinjas.GenericTree.GenericTree import GenericTree
from Utils.Array import input_array

"""
Given two Generic trees,return true if they are structurally identical
i.e. they are made of nodes with the same values arranged in the same way.


Input format :
    Line 1 : Tree 1 elements in level order form separated by space (as per done in class).
    Line 2 : Tree 2 elements in level order form separated by space (as per done in class).
    Order is - Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element

Output format :
    true or false
"""


def is_structurally_identical(root_a, root_b) -> bool:
    if root_a is None and root_b is None:  # both None, then they are identical
        return True
    elif root_a is None or root_b is None:  # not both but either of them is None -> Non-Identical
        return False

    # Both are not None, so check the root matches and then check if subtrees matches

    # both root should have same data and same no of childerns
    if root_a.data != root_b.data or \
            len(root_a.children) != len(root_b.children):
        return False

    children_count = len(root_b.children)  # or len(root_a.children)
    for i in range(children_count):
        child_a = root_a.children[i]
        child_b = root_b.children[i]
        identical = is_structurally_identical(child_a, child_b)
        if not identical:
            return False  # else keep on checking for other children pairs

    return True  # if not yet returned


if __name__ == '__main__':
    tree_root_a = GenericTree.single_line_input(input_array(""))
    tree_root_b = GenericTree.single_line_input(input_array(""))
    print(is_structurally_identical(tree_root_a, tree_root_b))

"""
10 3 20 30 40 2 40 50 0 0 0 0 
10 3 20 30 40 2 40 50 0 0 0 0
True <<< Output

10 3 20 30 40 2 40 50 0 0 0 0 
10 3 2 30 40 2 40 50 0 0 0 0
False <<< Output
"""
