from GenericTree import GenericTree

# Code : Number of nodes greater than x
from Utils.Array import input_array


def count_nodes_greater_then_x(root, x) -> int:
    if root is None:
        return 0

    count = 1 if root.data > x else 0  # handling the root

    # asking results from subtrees
    for child in root.children:
        count += count_nodes_greater_then_x(child, x)

    return count


if __name__ == '__main__':
    array = input_array()
    value_x = array[0]
    del array[0]  # Removing the first element of the array, so remaining is the tree input
    tree_node = GenericTree.single_line_input(array)
    count = count_nodes_greater_then_x(tree_node, value_x)
    print(count)

"""
35 10 3 20 30 40 2 40 50 0 0 0 0
3       << OUTPUT

10 10 3 20 30 40 2 40 50 0 0 0 0
5       << OUTPUT
"""
