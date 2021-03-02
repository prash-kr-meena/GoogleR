from Tree.BinaryTree.BinaryTree import BinaryTree, BinaryTreeNode
from Utils.Array import input_array

"""
https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem       - Submitted Successfully

Here for the question, we are choosing WAY-2
We have done implementation with WAY-1 in GenericTree
"""


def find_height(root):
    if root is None:
        return 0

    # height of the leaf node will be considered 0,  in the WAY-1  of implementation we consider None's height 0
    # if we comment this if condition, will get height according to WAY-2
    if root.left is None and root.right is None:
        return 0

    left_height = find_height(root.left)
    right_height = find_height(root.right)
    return max(left_height, right_height) + 1


if __name__ == '__main__':
    tree_root = BinaryTree.single_line_input(input_array(""))
    print(find_height(tree_root))
    pass
"""
Height of a tree can be defined in no of ways
2 popular ways are

WAY 1

    with this we assume a tree with null (None), root will have a height of 0
           10       --> 1
      20   30   40  --> 2
    40 50           --> 3


WAY 2
           10       --> 0
      20   30   40  --> 1
    40 50           --> 2


You can define how ever you want though

           10       --> 9
      20   30   40  --> 10
    40 50           --> 11



1 2 3 4 5 -1 -1 6 7 -1 -1 -1 -1 -1 -1
         1
        / \
      2    3         Height = 3
     / \
    4   5
    |
   / \
  6   7

"""
