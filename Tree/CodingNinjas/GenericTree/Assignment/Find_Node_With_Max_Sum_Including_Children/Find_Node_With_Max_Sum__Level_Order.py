from Tree.CodingNinjas.GenericTree.GenericTree import GenericTree, GenericTreeNode
from collections import deque
from Utils.Array import input_array


# Very easy compared to Recursive approach
# For finding such sum, we would require level_order_traversal
def find_node_with_max_sum_including_children(root) -> GenericTreeNode:
    max_sum = float("-inf")
    max_node = None  # Temporary

    queue = deque()
    queue.append(root)
    while len(queue) != 0:
        curr_root = queue.popleft()
        curr_root_sum = curr_root.data
        # print(curr_root.data)     # print level-order to first check if you have written correct level-order-traversal
        for child in curr_root.children:
            curr_root_sum += child.data
            queue.append(child)

        if curr_root_sum > max_sum:
            max_sum = curr_root_sum
            max_node = curr_root

    print("Max Sum :", max_sum)
    return max_node


if __name__ == '__main__':
    array = input_array()
    tree_root = GenericTree.single_line_input(array)
    node = find_node_with_max_sum_including_children(tree_root)
    print(node.data)

"""
10 3 2 3 4 2 100 200 1 5 1 8 0 0 0 0
2 <<<<< MaxSum 302

5 3 1 2 3 1 15 2 4 5 1 6 0 0 0 0
1 <<<<< MaxSum 16
"""
