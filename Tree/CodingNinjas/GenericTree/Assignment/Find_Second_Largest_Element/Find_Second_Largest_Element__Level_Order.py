from collections import deque

from Tree.CodingNinjas.GenericTree.GenericTree import GenericTree, GenericTreeNode
from Utils.Array import input_array

"""
Here instead of calling the predefined method after collecting all elements as list,
we can embed the logic here only

Two Test Cases Filed : For Output like these
10 0                Only One Node
-2147483648     <<  Expected
-inf            <<  Output 
"""


# Always first write the level-order traversal, then go for modifying and solving the problem
def find_2nd_largest_element__extra_space(root: GenericTreeNode) -> int:
    if root is None:
        return None

    first_largest = second_largest = float("-inf")
    # --------------------------------------------
    queue = deque()
    queue.append(root)
    while len(queue) != 0:
        curr_root = queue.popleft()
        # print(curr_root.data)     # Printing Level Order

        # Embdding the logic here
        if curr_root.data > first_largest:
            second_largest = first_largest
            first_largest = curr_root.data
        elif curr_root.data > second_largest and curr_root.data != first_largest:  # handling duplicity
            second_largest = curr_root.data

        for child in curr_root.children:
            queue.append(child)

    return second_largest
    # --------------------------------------------


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
