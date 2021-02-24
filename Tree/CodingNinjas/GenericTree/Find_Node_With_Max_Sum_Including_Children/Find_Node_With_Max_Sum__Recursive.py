from Tree.CodingNinjas.GenericTree.GenericTree import GenericTree, GenericTreeNode
from collections import deque
from Utils.Array import input_array

"""
With recursion this problem, becomes a little tricky
as now you would need to get both the node and the sum of it,
because we need to compare the sum's but need to return the actual node

so we will actually be returning a tuple of Node and the sum
"""


# We can also implement the same using recursive approach
def find_node_with_max_sum_including_children(root) -> (GenericTreeNode, int):
    if root is None:
        return None

    max_node_sum = float("-inf")
    max_node = None

    # Finding total sum for current root
    curr_root_sum = root.data
    for child in root.children:
        curr_root_sum += child.data

    if curr_root_sum > max_node_sum:
        max_node = root
        max_node_sum = curr_root_sum

    # Finding total sum for current root's children
    for child in root.children:
        node_sum_pair = find_node_with_max_sum_including_children(child)
        if node_sum_pair[1] > max_node_sum:  # get sum
            max_node = node_sum_pair[0]  # get node
            max_node_sum = node_sum_pair[1]

    return max_node, max_node_sum  # tuple (node, sum)


def find_node_with_max_sum_including_children_helper(root):
    pair = find_node_with_max_sum_including_children(root)
    print("node:", pair[0].data, " | sum : ", pair[1])
    return pair[0].data  # the node


if __name__ == '__main__':
    array = input_array()
    tree_root = GenericTree.single_line_input(array)
    node = find_node_with_max_sum_including_children_helper(tree_root)
    print(node)

"""
10 3 2 3 4 2 100 200 1 5 1 8 0 0 0 0
"""
