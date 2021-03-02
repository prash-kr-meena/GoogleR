from collections import deque

from Tree.BinaryTree.BinaryTree import BinaryTree, BinaryTreeNode
from Utils.Array import input_array


def level_order_one_line(root) -> None:
    queue = deque()
    queue.append(root)
    while len(queue) != 0:
        curr_root = queue.popleft()
        print(curr_root.data, end=" ")

        if curr_root.left is not None:
            queue.append(curr_root.left)

        if curr_root.right is not None:
            queue.append(curr_root.right)


def level_order_separate_line(root) -> None:  # only adding few lines in above code
    queue = deque()
    queue.append(root)
    while len(queue) != 0:
        size = len(queue)  # added
        while size != 0:  # added
            curr_root = queue.popleft()
            print(curr_root.data, end=" ")

            if curr_root.left is not None:
                queue.append(curr_root.left)

            if curr_root.right is not None:
                queue.append(curr_root.right)

            size -= 1  # added
        print()  # added


if __name__ == '__main__':
    tree_root = BinaryTree.single_line_input(input_array(""))
    BinaryTree.display(tree_root)
    level_order_one_line(tree_root)
    print("\n")
    level_order_separate_line(tree_root)

"""
                        1
                    2      3
                  4   5      6
                7      8   

1 2 3 4 5 -1 6 7 -1 -1 8 -1 -1 -1 -1 -1 -1  

"""
