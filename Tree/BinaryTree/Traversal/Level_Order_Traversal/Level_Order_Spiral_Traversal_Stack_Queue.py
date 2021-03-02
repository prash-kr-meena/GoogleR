from collections import deque

from Tree.BinaryTree.BinaryTree import BinaryTree, BinaryTreeNode
from Utils.Array import input_array

"""

   <.......     1    <.......           LEFT 
   |           / \ 
   .....>>    2    3 ..........>>       RIGHT
            / \   / \            \ 
    <..... 7  6  5   4  <<......./      LEFT

1 2 3 7 6 5 4 -1 -1 -1 -1 -1 -1 -1 -1 

now to get the elements in the same order : we use queue, Which we also use in the normal level-order-traversal
and to get the, revere-order we need to use stack

So we would store the first element 1 (root) in the stack 
then 2, 3 in the queue
and then 7 7 5 4 on stack,

One think to keep in mind, when you will be reading from one of the data-structure you will be updating and pushing 
into another data-structure

you would need a way to alternate bw these two data-structures
"""


def level_order_separate_line(root) -> None:  # only adding few lines in above code
    queue = deque()
    stack = deque()  # stack using deque()      we could also use a list []
    stack.append(root)

    go_alternate = True  # so as to choose stack initially, instead of queue

    while len(queue) != 0 or len(stack) != 0:  # if any one is not empty, go and process
        if go_alternate:
            # you read from stack(top) and push to queue (back)
            while len(stack) != 0:
                curr_root = stack.pop()
                print(curr_root.data, end=" ")  # process

                # push left and right to the different structure - here queue
                if curr_root.left is not None:
                    queue.append(curr_root.left)
                if curr_root.right is not None:
                    queue.append(curr_root.right)

            # go in other direction
            go_alternate = not go_alternate  # Should be outside of the while loop
        else:
            # you read from queue (front) and push to stack (top)
            while len(queue) != 0:
                curr_root = queue.popleft()
                print(curr_root.data, end=" ")  # process

                # push left and right to the different structure - here queue
                if curr_root.left is not None:
                    stack.append(curr_root.left)
                if curr_root.right is not None:
                    stack.append(curr_root.right)

            # go in other direction
            go_alternate = not go_alternate  # Should be outside of the while loop


if __name__ == '__main__':
    tree_root = BinaryTree.single_line_input(input_array(""))
    BinaryTree.display(tree_root)
    level_order_separate_line(tree_root)

"""
                        1
                    2      3
                  4   5      6
                7      8   

1 2 3 4 5 -1 6 7 -1 -1 8 -1 -1 -1 -1 -1 -1  

"""
