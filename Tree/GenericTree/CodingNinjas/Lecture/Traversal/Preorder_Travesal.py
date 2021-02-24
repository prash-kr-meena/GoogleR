from Tree.GenericTree.GenericTree import GenericTree
from Utils.Array import input_array


# First Root, then children
def preorder_traversal(root) -> None:
    if root is None:
        return

    print(root.data, end=" ")
    for child in root.children:
        preorder_traversal(child)


if __name__ == '__main__':
    array = input_array()
    tree_root = GenericTree.single_line_input(array)
    preorder_traversal(tree_root)

"""
10 3 20 30 40 2 40 50 0 0 0 0

           10
      20   30   40
    40 50
"""
