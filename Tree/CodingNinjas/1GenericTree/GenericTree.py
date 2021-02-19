from collections import deque

from Utils.Array import input_array


class GenericTreeNode:
    # This tree, allows any number of child nodes
    def __init__(self, data):
        self.data = data
        self.children = []  # list of TreeNode


class GenericTree:

    @staticmethod
    def input_interactive() -> GenericTreeNode:
        """

                            2
                         /  |  \
                       /    |    \
                     /      |     \
                   3        4        0
                 5  6     7  8
                9        1

        2
        3
        3 4 0
        2
        5 6
        2
        7 8
        0
        1
        9
        0
        1
        1
        0
        0
        0
        """
        root_value = int(input("Enter Root : "))
        root_node = GenericTreeNode(root_value)

        queue = deque()  # push at end, pop from front
        queue.append(root_node)

        while len(queue) != 0:  # queue is not empty
            curr_root = queue.popleft()

            print(curr_root.data, "'s child count : ", end="")
            child_count = int(input())
            if child_count == 0:
                continue

            print("Children of " + str(curr_root.data))
            children = input_array()
            for child in children:
                child_node = GenericTreeNode(child)
                curr_root.children.append(child_node)
                queue.append(child_node)

        return root_node  # The original root, Not modified

    @staticmethod
    def input_one_line() -> GenericTreeNode:
        """

                            2
                         /  |  \
                       /    |    \
                     /      |     \
                   3        4        0
                 5  6     7  8
                9        1

        2 3 3 4 0 2 5 6 2 7 8 0 1 9 0 1 1 0 0 0
        """
        input_pointer = 0
        one_line_input = input_array("")  # element could denote, node_value, no_of_children

        root_value = one_line_input[input_pointer]  # First element will be root
        input_pointer += 1
        root_node = GenericTreeNode(root_value)

        queue = deque()  # push at end, pop from front
        queue.append(root_node)

        while len(queue) != 0:  # queue is not empty
            curr_root = queue.popleft()

            child_count = one_line_input[input_pointer]  # curr_root's child count
            input_pointer += 1
            if child_count == 0:
                continue

            # Children of curr_root
            for i in range(child_count):
                child_value = one_line_input[input_pointer]
                input_pointer += 1
                child_node = GenericTreeNode(child_value)
                curr_root.children.append(child_node)
                queue.append(child_node)

        return root_node  # The original root, Not modified

    @staticmethod
    def print_level_order_detailed(root_node) -> None:
        queue = deque()
        queue.append(root_node)

        while len(queue) != 0:
            curr_root_node = queue.popleft()

            children_values = []  # for printing at once, without extra comma
            for child_node in curr_root_node.children:
                children_values.append(str(child_node.data))
                queue.append(child_node)

            print(curr_root_node.data, ": ", ", ".join(children_values))

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
                for child_node in curr_root_node.children:
                    queue.append(child_node)
                window_size -= 1  # decrementing window
            print()  # after window size is over


if __name__ == '__main__':
    root = GenericTree.input_one_line()
    GenericTree.print_level_order(root)
    # root = GenericTree.input_interactive()
    # GenericTree.print_level_order_detailed(root)

"""
                            2
                         /  |  \
                       /    |    \
                     /      |     \
                   3        4        0
                 5  6     7  8
                9        1

2 3 3 4 0 2 5 6 2 7 8 0 1 9 0 1 1 0 0 0

--------------------
1 10 10 20 30 40 50 60 70 80 90 100 1 110 1 120 1 130 1 140 1 150 1 160 1 170 1 180 1 190 1 200 1 220 0 0 0 0 0 0 0 0 0 1 230 1 270 2 300 390 0 0

                                            1
         10      20      30      40      50      60      70      80      90      100
        100     120     130     140     150     160      170    180      190     200
        220
        230
        270
      300 390
"""
