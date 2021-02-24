from collections import deque

from Tree.CodingNinjas.GenericTree.GenericTree import GenericTree, GenericTreeNode
from Utils.Array import input_array


# Always first write the level-order traversal, then go for modifying and solving the problem
def find_2nd_largest_element__extra_space(root: GenericTreeNode):
    if root is None:
        return
    # --------------------------------------------
    queue = deque()
    queue.append(root)
    while len(queue) != 0:
        curr_root = queue.popleft()
        # print(curr_root.data)     # Printing Level Order
        for child in curr_root.children:
            queue.append(child)

    # --------------------------------------------


if __name__ == '__main__':
    tree_root = GenericTree.single_line_input(input_array(""))
    print(find_2nd_largest_element__extra_space(tree_root))
    pass

"""
10 3 20 30 40 2 40 50 0 0 0 0 
40  << Output
"""
