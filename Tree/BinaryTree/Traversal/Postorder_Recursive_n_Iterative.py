from Tree.BinaryTree.BinaryTree import BinaryTree
from Utils.Array import input_array

"""
Rachit Jain's Video : https://www.youtube.com/watch?v=5BzvEmscu-o&ab_channel=RachitJain
My Github Changes : https://github.com/prash-kr-meena/DataStructures-Algorithms/commit/7c94849b915d25f3a6facdad99b9fd5d6d92e8cf

"""


def do_postorder_traversal(root) -> None:
    if root is None:
        return None

    do_postorder_traversal(root.left)
    do_postorder_traversal(root.right)
    print(root.data, end=" ")


def do_postorder_traversal_iteratively(root) -> None:
    stack = []
    stack.append((root, 0))

    while len(stack) != 0:
        curr_root, curr_root_state = stack.pop()

        if curr_root is None or curr_root_state == 3:
            continue

        stack.append((curr_root, curr_root_state + 1))

        if curr_root_state == 0:
            stack.append((curr_root.left, 0))
        elif curr_root_state == 1:
            stack.append((curr_root.right, 0))
        elif curr_root_state == 2:
            print(curr_root.data, end=" ")


if __name__ == '__main__':
    tree_root = BinaryTree.single_line_input(input_array(""))
    BinaryTree.display(tree_root)
    do_postorder_traversal(tree_root)
    print()
    do_postorder_traversal_iteratively(tree_root)

"""
                        1
                    2      3
                  4   5      6
                7      8   

1 2 3 4 5 -1 6 7 -1 -1 8 -1 -1 -1 -1 -1 -1  

"""
