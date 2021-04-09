from Tree.BinaryTree.BinaryTree import BinaryTree, BinaryTreeNode
from Utils.Array import input_array

"""
LeetCode : https://leetcode.com/problems/diameter-of-binary-tree/
GFG: https://www.geeksforgeeks.org/diameter-of-a-binary-tree/
"""

diameter = 0


def find_depth(root: BinaryTreeNode) -> int:
    if root is None:
        return 0

    left_depth = find_depth(root.left)
    right_depth = find_depth(root.right)
    return max(left_depth, right_depth) + 1  # maximum_depth


def diameter_of_binary_tree(root: BinaryTreeNode) -> int:
    if root is None:
        return 0

    left_child_diameter = diameter_of_binary_tree(root.left)
    right_child_diameter = diameter_of_binary_tree(root.right)

    # current node's diameter
    left_depth = find_depth(root.left)
    right_depth = find_depth(root.right)
    curr_node_diameter = left_depth + right_depth

    return max(curr_node_diameter, left_child_diameter, right_child_diameter)


if __name__ == '__main__':
    tree_input = input_array(prompt="")
    root = BinaryTree.single_line_input(tree_input)
    BinaryTree.display(root)
    print("diameter : ", diameter_of_binary_tree(root))

"""
            1
          /   \
        2      3
      /  \
    4     5
    
1 2 3 4 5 -1 -1 -1 -1 -1 -1
"""

"""
          0
         / \ 
        1   2
       / \ 
      3   4
    /      \
   5        6
             \
              7
0 1 2 3 4 -1 -1 5 -1 -1 6 -1 -1 -1 7 -1 -1 
"""
