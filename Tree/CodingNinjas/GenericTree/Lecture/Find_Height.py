from sys import setrecursionlimit
from Tree.CodingNinjas.GenericTree.GenericTree import GenericTree
from Utils.Array import input_array


def find_height(root) -> int:
    if root is None:
        return 0

    max_subtree_height = 0  # getting the max height of children nodes
    for child in root.children:
        max_subtree_height = max(max_subtree_height, find_height(child))

    return max_subtree_height + 1  # 1 for the root


if __name__ == '__main__':
    setrecursionlimit(11000)
    array = input_array()
    tree_root = GenericTree.single_line_input(array)
    height = find_height(tree_root)
    print(height)

"""
Height of a tree can be defined in no of ways
2 popular ways are


10 3 20 30 40 2 40 50 0 0 0 0

WAY 1   (We choose this)
    with this we assume a tree with null (None), root will have a height of 0
           10      --> 1
      20   30   40 --> 2
    40 50          --> 3


WAY 2
           10      --> 0
      20   30   40 --> 1
    40 50          --> 2


You can define how ever you want though

           10      --> 9
      20   30   40 --> 10
    40 50          --> 11

"""
