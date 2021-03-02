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


We can get the same results if we use 2 stacks          {   ie instead of popleft() use pop()  } 

Things we would need to care about : 
1. is the inserting order, 
    in case of the stack_queue implementation we were always inserting left_child first and then right_child
    But here things will change
"""


def level_order_separate_line(root) -> None:  # only adding few lines in above code
    stack_1 = deque()
    stack_2 = deque()
    stack_2.append(root)

    go_alternate = True  # so as to choose stack_2 initially, instead of stack_1

    while len(stack_1) != 0 or len(stack_2) != 0:  # if any one is not empty, go and process
        if go_alternate:
            # you read from stack_2(top) and push to stack_1 (back)
            while len(stack_2) != 0:
                curr_root = stack_2.pop()
                print(curr_root.data, end=" ")  # process

                # push right and left to the different structure - here stack_1
                if curr_root.right is not None:
                    stack_1.append(curr_root.right)
                if curr_root.left is not None:
                    stack_1.append(curr_root.left)

            # go in other direction
            go_alternate = not go_alternate  # Should be outside of the while loop
        else:
            # you read from stack_1 (front) and push to stack_2 (top)
            while len(stack_1) != 0:
                curr_root = stack_1.pop()
                print(curr_root.data, end=" ")  # process

                # push left and right to the different structure - here stack_1
                if curr_root.left is not None:
                    stack_2.append(curr_root.left)
                if curr_root.right is not None:
                    stack_2.append(curr_root.right)

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
