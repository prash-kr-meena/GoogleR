from Tree.GenericTree.GenericTree import GenericTree

from Utils.Array import input_array


# First children, then root
def postorder_traversal(root) -> None:
    if root is None:
        return

    for child in root.children:
        postorder_traversal(child)

    print(root.data, end=" ")


if __name__ == '__main__':
    array = input_array()
    tree_root = GenericTree.single_line_input(array)
    postorder_traversal(tree_root)

"""
10 3 20 30 40 2 40 50 0 0 0 0

           10
      20   30   40
    40 50
"""
