class GenericTreeNode:
    """
    This tree, allows any number of child nodes
    """

    def __init__(self, data):
        self.data = data
        self.children = []  # list of TreeNode


if __name__ == '__main__':
    root_node = GenericTreeNode(4)
    root_node.children.append()
