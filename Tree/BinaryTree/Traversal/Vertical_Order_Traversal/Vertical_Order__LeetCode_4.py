from typing import Dict
from Tree.BinaryTree.BinaryTree import BinaryTree, BinaryTreeNode
from Utils.Array import input_array, print_array_multiline, print_array_inline

"""
__1__
/     \
2_     6
  \   /
  7_ 3
 /  \
 4  5
   /
   8   

1 2 6 -1 7 3 -1 4 5 -1 -1 -1 -1 8 -1 -1 -1

2 4
1 7 3 8        <<< The order is correct here, 7 3 are on same level and are printed from left to right,  
6 5                                           as we are doing level order traversal


But if the requirement of the question is, that for elements on the same level, you need to print them in sorted order
ie, it should be [1 3 7 8]  instead of [1 7 3 8] 

Then our solution will not work

This what the requirement in the leet-code question is : 
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
"""

"""
The Below solution doesn't work
I wanted a way to use my earlier solutions only

This is just a scratch solution, where idea is from the youtube video :
https://www.youtube.com/watch?v=kqHNP6NTzME&ab_channel=TECHDOSE
"""


def pre_order__to__fill_x_y_for_each_node(root, x_y_table: Dict[int, list], horizontal_distance=0,
                                          vertical_distance=0) -> None:
    if root is None:
        return

    # Process Node
    # instead of printing, we need to store x,y in the map ie dictionary
    if x_y_table.get(horizontal_distance) is None:
        # create the mapping
        x_y_table[horizontal_distance] = list()  # new empty list
        x_y_table[horizontal_distance].append(root.data)  # append this vertical distance to the list
    else:
        # mapping already present
        x_y_table[horizontal_distance].append(root.data)  # append this vertical distance to the list

    pre_order__to__fill_x_y_for_each_node(root.left, x_y_table, horizontal_distance - 1, vertical_distance + 1)
    pre_order__to__fill_x_y_for_each_node(root.right, x_y_table, horizontal_distance + 1, vertical_distance + 1)


def vertical_order(root):
    x_y_table: Dict[int, list] = dict()  # map of number, list
    pre_order__to__fill_x_y_for_each_node(root, x_y_table)

    for x in sorted(x_y_table.keys()):
        print_array_inline(x_y_table[x])
        # print(f"{x} : {x_y_table[x]}")


if __name__ == '__main__':
    tree_root = BinaryTree.single_line_input(input_array(""))
    BinaryTree.display(tree_root)
    vertical_order(tree_root)

"""
The idea is to do a bfs approach,
and while traversing in a BFS way, for each node maintain its (x,y) variables
x = horizontal distance :   we assume root to start at 0,
                            so, its left_child will be 1 unit left ie -1
                            and right_child will be 1 unit right ie +1
y = vertical distance : depth of each node at each vertical level
                        ie, root is at depth 0, then its children are at depth 1 and so on

so, for root, both x and y are 0

If the two nodes have same horizontal distance, then it means that they are on the same-vertical-line
like how we, can say, if two nodes have depth (vertical_distance) then the are at same-horizontal-line



once we do a traversal, and have a state of x,y with each of the node
we realize that, after recursion these will vanish
so we need to persist these separately so that we can go for each of the horizontal_distance_value from left to right
"""
