from collections import deque

from Tree.BinaryTree.BinaryTree import BinaryTree
from Utils.Array import input_array


def right_view_of_binary_tree(root):
    queue = deque()
    queue.append(root)

    while len(queue) != 0:
        size = len(queue)
        pointer = 0  # start index with 0
        while pointer != size:
            curr_root = queue.popleft()
            if pointer == size - 1:  # print last element
                print(curr_root.data, end=" ")

            if curr_root.left is not None:
                queue.append(curr_root.left)

            if curr_root.right is not None:
                queue.append(curr_root.right)

            pointer += 1
        # ended a level

    pass


if __name__ == '__main__':
    tree_root = BinaryTree.single_line_input(input_array(""))
    BinaryTree.display(tree_root)
    right_view_of_binary_tree(tree_root)

"""
1 2 3 4 5 -1 6 7 -1 -1 8 -1 -1 -1 -1 -1 -1
"""
