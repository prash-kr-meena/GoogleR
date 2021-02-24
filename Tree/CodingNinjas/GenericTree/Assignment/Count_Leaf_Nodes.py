from Tree.CodingNinjas.GenericTree.GenericTree import GenericTree

from Utils.Array import input_array


def count_leaf_nodes(root) -> int:
    if root is None:  # Edge case
        return 0

    if len(root.children) == 0:
        return 1
        # There are no children to traverse, so return

    no_of_leaf_nodes = 0
    for child in root.children:  # handling subtrees
        no_of_leaf_nodes += count_leaf_nodes(child)

    return no_of_leaf_nodes


if __name__ == '__main__':
    array = input_array()
    tree_root = GenericTree.single_line_input(array)
    print(count_leaf_nodes(tree_root))

"""
10 3 20 30 40 2 40 50 0 0 0 0

           10
      20   30   40
    40 50
"""
