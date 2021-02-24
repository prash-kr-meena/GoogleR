from collections import deque

from Tree.GenericTree.GenericTree import GenericTree, GenericTreeNode
from Utils.Array import input_array


# Submitted successfully

# Remember :  Always just first write the level-order traversal, then start to modify and solve
def next_largest_element(root: GenericTreeNode, n) -> int:
    next_largest_node_data = None  # if not found return None
    difference = float("inf")  # as we need to minimize it

    # ------------------------------------
    queue = deque()
    queue.append(root)

    while len(queue) != 0:
        curr_root = queue.popleft()
        # process the current-root of tree
        if curr_root.data > n:
            difference_with_this_node = curr_root.data - n
            if difference_with_this_node < difference:  # minimizing difference
                difference = difference_with_this_node
                next_largest_node_data = curr_root.data

        # print(curr_root.data)     # to print level-order
        for child in curr_root.children:
            queue.append(child)
    # ------------------------------------

    return next_largest_node_data


if __name__ == '__main__':
    n = int(input("num :"))
    tree_root = GenericTree.single_line_input(input_array(""))
    print(next_largest_element(tree_root, n))

"""
18
10 3 20 30 40 2 40 50 0 0 0 0


21
10 3 20 30 40 2 40 50 0 0 0 0 

"""
