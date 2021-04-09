from Tree.BinaryTree.BinaryTree import BinaryTree
from Utils.Array import input_array

"""
Rachit Jain's Video : https://www.youtube.com/watch?v=5BzvEmscu-o&ab_channel=RachitJain
My Github Changes : https://github.com/prash-kr-meena/DataStructures-Algorithms/commit/7c94849b915d25f3a6facdad99b9fd5d6d92e8cf

"""


def go_inorder(root) -> None:
    if root is None:
        return

    go_inorder(root.left)
    print(root.data, end=" ")
    go_inorder(root.right)


"""
We have 3 states, for each of the node, We initialize the state with 0, as starting state

  In case of Inorder they will be
    0 = Going in Left direction
    1 = Processing
    2 = Going in Right direction
    3 = Done All processing, we can safely pop it out
"""


def go_inorder_iteratively(root) -> None:
    stack = [(root, 0)]  # Creating stack & Pushing a Pair of (node, its_state)

    while len(stack) != 0:
        curr_root, curr_root_state = stack.pop()

        if curr_root is None or curr_root_state == 3:
            # curr_root is popped out of the stack, and not pushed
            continue

        stack.append((curr_root, curr_root_state + 1))  # pushed curr_root with updated state

        if curr_root_state == 0:
            stack.append((curr_root.left, 0))
        elif curr_root_state == 1:
            print(curr_root.data, end=" ")
        elif curr_root_state == 2:
            stack.append((curr_root.right, 0))


if __name__ == '__main__':
    tree_input = input_array(prompt="")
    tree_root = BinaryTree.single_line_input(tree_input)
    BinaryTree.display(tree_root)
    go_inorder(tree_root)
    print()
    go_inorder_iteratively(tree_root)

"""
                        1
                    2      3
                  4   5      6
                7      8   

1 2 3 4 5 -1 6 7 -1 -1 8 -1 -1 -1 -1 -1 -1  
"""
