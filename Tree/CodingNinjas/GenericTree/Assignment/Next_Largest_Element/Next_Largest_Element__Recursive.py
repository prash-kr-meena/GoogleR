from Tree.CodingNinjas.GenericTree.GenericTree import GenericTree, GenericTreeNode
from Utils.Array import input_array


def next_largest_element(root, n) -> (GenericTreeNode, int):  # denoting (node.data, difference)
    if root is None:
        return None, None

    next_largest_node = None  # if not found return None
    total_difference = float("inf")  # as we need to minimize it

    # process the root
    if root.data > n:
        difference_with_this_node = root.data - n
        if difference_with_this_node < total_difference:  # minimizing total_difference
            total_difference = difference_with_this_node
            next_largest_node = root

    # process root's children
    for child in root.children:
        child_node, difference_for_child_node = next_largest_element(child, n)

        # similar to above logic
        if child_node.data > n:
            if difference_for_child_node < total_difference:  # minimizing total_difference
                total_difference = difference_for_child_node
                next_largest_node = child_node

    return next_largest_node, total_difference


if __name__ == '__main__':
    n = int(input("num :"))
    tree_root = GenericTree.single_line_input(input_array(""))
    next_largest, min_difference = next_largest_element(tree_root, n)
    print(next_largest.data)

"""
18
10 3 20 30 40 2 40 50 0 0 0 0 


21
10 3 20 30 40 2 40 50 0 0 0 0 

"""
