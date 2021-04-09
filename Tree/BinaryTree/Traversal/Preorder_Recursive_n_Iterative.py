from Tree.BinaryTree.BinaryTree import BinaryTree
from Utils.Array import input_array

"""
Rachit Jain's Video : https://www.youtube.com/watch?v=5BzvEmscu-o&ab_channel=RachitJain
My Github Changes : https://github.com/prash-kr-meena/DataStructures-Algorithms/commit/7c94849b915d25f3a6facdad99b9fd5d6d92e8cf

"""


def go_preorder(root) -> None:
    if root is None:
        return None

    print(root.data, end=" ")
    go_preorder(root.left)
    go_preorder(root.right)


"""
We have 3 states, for each of the node
we initialize the state with 0, as starting

  In case of Inorder they will be
    0 = Processing
    1 = Going in one direction
    2 = Going in another direction
    3 = Done All processing, we can safely pop it out
"""


# Using list as stack ie, append(), pop(), stack[-1], len(stack)
def go_preorder_iteratively(root_node):
    stack = [(root_node, 0)]  # Creating stack & Pushing a Pair of (node, its_state)

    while len(stack) != 0:
        curr_root, curr_root_state = stack.pop()

        # Notice : we have popped out the pair
        # so now we need to push its updated state, into the stack, But that we do only when
        # The state is less then 3 and its not a `None` Node

        # None Check, because while pushing into the stack, we do not have any None check, on the left or right of tree
        if curr_root is None or curr_root_state == 3:
            # continue, because we have already popped it out earlier, so nothing has to be popped
            continue

        # updating the, state of this node, and pushing it back
        # Now we will be processing this node, <We have the data with us> so we need to push the updated status
        # There is a reason, We push it back to stack, before actually doing the operations on the basis os state
        # and that reason is basically, to get order right
        stack.append((curr_root, curr_root_state + 1))

        if curr_root_state == 0:  # process node : as preorder
            print(curr_root.data, end=" ")

        elif curr_root_state == 1:  # go left : as preorder
            stack.append((curr_root.left, 0))  # Putting the new node at the starting state, State=0 Notice

        elif curr_root_state == 2:  # go right : as preorder
            stack.append((curr_root.right, 0))  # Putting the new node at the starting state, State=0 Notice


if __name__ == '__main__':
    tree_input = input_array(prompt="")
    tree_root = BinaryTree.single_line_input(tree_input)
    BinaryTree.display(tree_root)

    go_preorder(tree_root)
    print()
    go_preorder_iteratively(tree_root)

"""
                        1
                    2      3
                  4   5      6
                7      8 
1 2 3 4 5 -1 6 7 -1 -1 8 -1 -1 -1 -1 -1 -1  
"""
