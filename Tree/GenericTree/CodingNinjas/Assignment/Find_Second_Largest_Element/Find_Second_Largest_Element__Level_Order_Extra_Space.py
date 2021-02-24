from collections import deque

from Array.Final450.Find_First_Second__Smallest_n_Largest.Find_First_And_Second_Largest import \
    find_first_and_second_largest
from Tree.GenericTree.GenericTree import GenericTree, GenericTreeNode
from Utils.Array import input_array

"""
The idea, here is to traverse the tree and collect all the node's data in one list
and then apply a pre-written method to solve the problem of finding-2nd-largest


Two Test Cases Filed : For Output like these
10 0                Only One Node
-2147483648     <<  Expected
-inf            <<  Output   
"""


# Always first write the level-order traversal, then go for modifying and solving the problem
def find_2nd_largest_element__extra_space(root: GenericTreeNode) -> int:
    if root is None:
        return None  # no first or second largest exists

    tree_elements = []
    # --------------------------------------------
    queue = deque()
    queue.append(root)
    while len(queue) != 0:
        curr_root = queue.popleft()
        # print(curr_root.data)     # Printing Level Order
        tree_elements.append(curr_root.data)
        for child in curr_root.children:
            queue.append(child)

    # --------------------------------------------
    first_largest, second_largest = find_first_and_second_largest(tree_elements)
    return second_largest


if __name__ == '__main__':
    tree_root = GenericTree.single_line_input(input_array(""))
    print(find_2nd_largest_element__extra_space(tree_root))
    pass

"""
10 3 20 30 40 2 40 50 0 0 0 0 
40  << Output


10 0                Only One Node
-2147483648     <<  Expected
-inf            <<  Output
"""
