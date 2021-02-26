from Tree.BinaryTree.BinaryTree import BinaryTree
from Utils.Array import input_array

"""
Rachit Jain's Video : https://www.youtube.com/watch?v=5BzvEmscu-o&ab_channel=RachitJain
My Github Changes : https://github.com/prash-kr-meena/DataStructures-Algorithms/commit/7c94849b915d25f3a6facdad99b9fd5d6d92e8cf

"""


def do_inorder_traversal(root) -> None:
    if root is None:
        return

    do_inorder_traversal(root.left)
    print(root.data, end=" ")
    do_inorder_traversal(root.right)


"""
We have 3 states, for each of the node
we initialize the state with 0, as starting

  In case of Inorder they will be
    0 = Processing
    1 = Going in one direction
    2 = Going in another direction
    3 = Done All processing, we can safely pop it out
"""


def do_inorder_traversal_iteratively(root_node):
    stack = []  # using list as stack, ie, append(), pop(), stack[-1], len(stack)
    stack.append((root_node, 0))  # pushing a pair of (node, its_state)

    while len(stack) != 0:
        curr_root, curr_root_state = stack.pop()

        if curr_root_state == 0:
            # process node : as inorder
            pass
        elif curr_root_state == 1:
            # go left : as inorder
            pass
        elif curr_root_state == 2:
            # go right : as inorder
            pass
        else:
            pass
    pass


if __name__ == '__main__':
    tree_root = BinaryTree.single_line_input(input_array(""))
    BinaryTree.display(tree_root)
    do_inorder_traversal(tree_root)
    do_inorder_traversal_iteratively(tree_root)

"""
                        1
                    2      3
                  4   5      6
                7      8   

1 2 3 4 5 -1 6 7 -1 -1 8 -1 -1 -1 -1 -1 -1  
 
"""
