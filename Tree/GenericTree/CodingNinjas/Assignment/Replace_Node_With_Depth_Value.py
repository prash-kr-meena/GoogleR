from Tree.GenericTree.GenericTree import GenericTree
from Utils.Array import input_array

"""
In a given Generic Tree, replace each node with its depth value. 
You need to just update the data of each node, no need to return or print anything.
<No code for python was provided, so we need to print it as well>

Input format :
    Line 1 : Elements in level order form separated by space (as per done in class). 
    Order is - Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element


Sample Input 1 :
    10 3 20 30 40 2 40 50 0 0 0 0
    
Sample Output 1 : (Level wise, each level in new line)
    0
    1 1 1
    2 2
"""


# Replacing inplace - No need to return anything
# We need to maintain a variable, which will tell the depth at that level
# by default its 0, denoting depth of root is 0
def replace_node_with_depth_values(root, depth=0) -> None:
    if root is None:
        return

    root.data = depth  # processing the root

    for child in root.children:
        replace_node_with_depth_values(child, depth + 1)  # depth increases by a level


if __name__ == '__main__':
    array = input_array()
    tree_root = GenericTree.single_line_input(array)
    GenericTree.print_level_order(tree_root)
    replace_node_with_depth_values(tree_root)
    GenericTree.print_level_order(tree_root)

"""
10 3 20 30 40 2 40 50 0 0 0 0


1 1 2 2 30 4 1 5 1 60 1 70 1 8 1 9 1 100 0 0
"""
