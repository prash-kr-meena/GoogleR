from GenericTree import GenericTree
from Utils.Array import input_array


def find_sum_of_all_nodes(root):
    if root is None:
        return 0  # no nodes, so sum is 0

    subtree_sum = 0
    for child in root.children:
        subtree_sum += find_sum_of_all_nodes(child)

    total_sum = subtree_sum + root.data
    return total_sum


if __name__ == '__main__':
    root = GenericTree.single_line_input(input_array(""))
    # GenericTree.print_level_order(root)
    print(find_sum_of_all_nodes(root))

"""
10 3 20 30 40 2 40 50 0 0 0 0
190
"""
