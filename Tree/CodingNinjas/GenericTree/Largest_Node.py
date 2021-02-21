import sys

from GenericTree import GenericTree, GenericTreeNode
from Utils.Array import input_array


def largest_nodes(root) -> int:
    if root is None:  # Edge case - No largest node
        return -sys.maxsize

    maximum_data = root.data
    for child_root in root.children:
        maximum_data = max(maximum_data, largest_nodes(child_root))

    return maximum_data


if __name__ == '__main__':
    array = input_array()
    tree_root = GenericTree.single_line_input(array)
    print(largest_nodes(tree_root))

"""
10 3 20 90 40 2 40 50 0 0 0 0

           10
      20   90   40
    40 50
"""
