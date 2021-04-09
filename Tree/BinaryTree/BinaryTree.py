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

            print(f"{curr_root.data}'s left child : ", end="")
            left_child_value = int(input())
            if left_child_value != -1:
                left_child_node = BinaryTreeNode(left_child_value)
                curr_root.left = left_child_node
                queue.append(left_child_node)

            print(f"{curr_root.data}'s right child : ", end="")
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

    @staticmethod
    def _display_aux(root_node):
        """
        Returns list of strings, width, height, and horizontal coordinate of the root.
        """

        # No child.
        if root_node.right is None and root_node.left is None:
            line = '%s' % root_node.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if root_node.right is None:
            lines, n, p, x = BinaryTree._display_aux(root_node.left)
            s = '%s' % root_node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if root_node.left is None:
            lines, n, p, x = BinaryTree._display_aux(root_node.right)
            s = '%s' % root_node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = BinaryTree._display_aux(root_node.left)
        right, m, q, y = BinaryTree._display_aux(root_node.right)
        s = '%s' % root_node.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    @staticmethod
    def display(root_node):
        lines, *_ = BinaryTree._display_aux(root_node)
        for line in lines:
            print(line)
        print("`````````````````````")


if __name__ == '__main__':
    # tree_root = BinaryTree.input_interactive()
    # BinaryTree.print_level_order_detailed(tree_root)

    tree_root = BinaryTree.single_line_input(input_array(""))
    BinaryTree.print_level_order(tree_root)
    BinaryTree.display(tree_root)

""" 
2 3 4 5 6 7 8 9 -1 -1 -1 -1 -1 -1 1 -1 -1 -1 -1

"""
