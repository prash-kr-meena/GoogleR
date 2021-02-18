"""

Given binary tree
create a mirror of that

           1                   |            1
        2      3              |         3     2
     4    5   6   7            |        7 6    5 4
            9                  |              9

1. is this a complete tree?
2. Do i need to build the tree?
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def help(root):
    mirror(root, root)


def mirror(root1, root2) -> None:
    if root1 is None and root2 is None:
        return None

    root1.left =  root2.right
    root1.right = root2.left

    mirror(root1.left, root2.right)
    mirror(root1.right, root2.left)


def mirror_out_of_place(self) -> TreeNode:
    # Todo
    pass


def print_tree(self):
    # Todo
    pass


def input_tree(self):
    # Todo
    pass
