from collections import deque

from Utils.Array import input_array


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None  # Point to BinaryTreeNode
        self.right = None  # Point to BinaryTreeNode


class BinaryTree:
    """
    Put -1 to denote that it doesn't have a child
    """

    @staticmethod
    def input_interactive() -> BinaryTreeNode:
        """
                         2
                       /  \
                     /      \
                   3         4
                 5  6       7  8
                9                 1
        """
        root_value = int(input("Enter Root : "))
        if root_value == -1:  # Creating a empty tree - ie None
            return None

        root_node = BinaryTreeNode(root_value)

        queue = deque()  # push at end, pop from front
        queue.append(root_node)

        while len(queue) != 0:  # queue is not empty
            curr_root = queue.popleft()

            print(curr_root.data, "'s left child : ", end="")
            left_child_value = int(input())
            if left_child_value != -1:
                left_child_node = BinaryTreeNode(left_child_value)
                curr_root.left = left_child_node
                queue.append(left_child_node)

            print(curr_root.data + "'s right child : ", end="")
            right_child_value = int(input())
            if right_child_value != -1:
                right_child_node = BinaryTreeNode(right_child_value)
                curr_root.right = right_child_node
                queue.append(right_child_node)

        return root_node  # The original root, Not modified

    @staticmethod
    def single_line_input(one_line_input) -> BinaryTreeNode:
        """
                         2
                       /  \
                     /      \
                   3         4
                 5  6       7  8
                9                 1
        2 3 4 5 6 7 8 9 -1 -1 -1 -1 -1 -1 1 -1 -1 -1 -1
        """
        input_pointer = 0
        root_value = one_line_input[input_pointer]  # First element will be root
        input_pointer += 1

        if root_value == -1:  # Creating a empty tree - ie None
            return None

        root_node = BinaryTreeNode(root_value)
        queue = deque()  # push at end, pop from front
        queue.append(root_node)

        while len(queue) != 0:  # queue is not empty
            curr_root = queue.popleft()

            left_child_value = one_line_input[input_pointer]  # curr_root's left child
            input_pointer += 1
            if left_child_value != -1:
                left_child_node = BinaryTreeNode(left_child_value)
                curr_root.left = left_child_node
                queue.append(left_child_node)

            right_child_value = one_line_input[input_pointer]  # curr_root's right child
            input_pointer += 1
            if right_child_value != -1:
                right_child_node = BinaryTreeNode(right_child_value)
                curr_root.right = right_child_node
                queue.append(right_child_node)

        return root_node  # The original root, Not modified

    @staticmethod
    def print_level_order_detailed(root_node) -> None:
        queue = deque()
        queue.append(root_node)

        while len(queue) != 0:
            curr_root_node = queue.popleft()

            left_node_value = right_node_value = "_"
            if curr_root_node.left is not None:
                queue.append(curr_root_node.left)
                left_node_value = curr_root_node.left.data

            if curr_root_node.right is not None:
                queue.append(curr_root_node.right)
                right_node_value = curr_root_node.right.data

            print(f"{curr_root_node.data} >  L {left_node_value}  |  R {right_node_value}")

    @staticmethod
    def print_level_order(root_node) -> None:
        # This method may look n^3, but its only n^2, top 2 while conditions are similar
        queue = deque()
        queue.append(root_node)

        while len(queue) != 0:  # while queue is not empty
            window_size = len(queue)
            while window_size != 0:  # window size, denoting elements at current level
                curr_root_node = queue.popleft()
                print(curr_root_node.data, end=" ")

                if curr_root_node.left is not None:
                    queue.append(curr_root_node.left)
                if curr_root_node.right is not None:
                    queue.append(curr_root_node.right)

                window_size -= 1  # decrementing window
            print()  # after window size is over


if __name__ == '__main__':
    # tree_root = BinaryTree.input_interactive()
    # BinaryTree.print_level_order_detailed(tree_root)

    tree_root = BinaryTree.single_line_input(input_array(""))
    BinaryTree.print_level_order(tree_root)

""" 
2 3 4 5 6 7 8 9 -1 -1 -1 -1 -1 -1 1 -1 -1 -1 -1

"""
