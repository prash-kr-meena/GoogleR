from typing import Dict
from Tree.BinaryTree.BinaryTree import BinaryTree, BinaryTreeNode
from Utils.Array import input_array, print_array_multiline, print_array_inline

"""
set 1 : https://www.geeksforgeeks.org/print-binary-tree-vertical-order/
    Time complexity : O(w*n)        where   w = width of Binary Tree ,
                                            n = number of nodes in Binary Tree.
    Worst case w = O(n) (consider a complete tree for example)
    and time complexity can become O(n^2).

set 2 : https://www.geeksforgeeks.org/print-binary-tree-vertical-order-set-2/
set 3 : https://www.geeksforgeeks.org/print-a-binary-tree-in-vertical-order-set-3-using-level-order-traversal/

"""

"""
The idea is to do a simple bfs approach,
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

for that reason we can pass in a dictionary
NOTE : i don't want to have a global dictionary, rather one that i can pass to the function
        and have its access in other function, from where ill pass it


About Dictionaries
Note : that the restriction with keys in Python dictionary is only immutable data types can be used as keys,
        which means we cannot use a dictionary of list as a key.

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
                       1
                      / \
                     2   3
                    / \   \
                   4   5   6
                  /     \
                 7       8   
1 2 3 4 5 -1 6 7 -1 -1 8 -1 -1 -1 -1 -1 -1

Output
7
4
2
1 5
8 3       <<  Note this order       Its Not correct, should be [3 8]
6
"""
