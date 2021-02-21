from GenericTree import GenericTree

from Utils.Array import input_array


def print_leaf_nodes(root):
    if root is None:  # Edge case
        return

    if len(root.children) == 0:
        print(root.data)

    for child in root.children:  # handling subtrees
        print_leaf_nodes(child)


if __name__ == '__main__':
    array = input_array()
    tree_root = GenericTree.single_line_input(array)
    print_leaf_nodes(tree_root)

"""
10 3 20 30 40 2 40 50 0 0 0 0

           10
      20   30   40
    40 50
"""
