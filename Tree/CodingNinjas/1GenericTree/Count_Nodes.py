from GenericTree import GenericTree
from Utils.Array import input_array


def count_nodes(root):
    if root is None:  # EDGE Case
        return 0

    count = 1  # for the root
    for child in root.children:  # Base case is intrinsically handled by the loop
        count += count_nodes(child)

    return count


if __name__ == '__main__':
    array = input_array()
    tree_root = GenericTree.single_line_input(array)
    print(count_nodes(tree_root))

"""
10 3 20 30 40 2 40 50 0 0 0 0

           10
      20   30   40
    40 50
"""
