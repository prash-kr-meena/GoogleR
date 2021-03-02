from typing import Dict

from Tree.BinaryTree.BinaryTree import BinaryTree
from Tree.BinaryTree.Traversal.Vertical_Order_Traversal.Vertical_Order_BFS_2 import finding_x_for_each_node__level_order
from Utils.Array import input_array, print_array_inline

"""
The prerequisite to solving this problem is to doing the vertical_order traversal
and from our vertical order traversal we will get a map (dictionary) of <int, list>
mapping the [[ horizontal_distance -> elements_in_vertical_line]]  

Now, note that this vertical line starts from the top and goes to bottom direction 

So, to get the bottom view of the tree
we need to print last_element from the list of elements_in_vertical_line
with the horizontal distance in sorted order

We can get rid of sorting, (n lg n) by doing a simple liner search to find the min_hd and max_hd
as we have done in the  Vertical_Order_BFS_Optimized_3.py


https://www.geeksforgeeks.org/bottom-view-binary-tree/
"""


def top_view_of_binary_tree(root):
    x_table: Dict[int, list] = dict()  # map of number, list
    finding_x_for_each_node__level_order(root, x_table)

    min_hd, max_hd = float("inf"), float("-inf")
    for key in x_table.keys():
        min_hd = min(min_hd, key)
        max_hd = max(max_hd, key)

    for i in range(min_hd, max_hd + 1):  # so that we include max_hd as well
        print(x_table[i][-1], end=" ")  # Notice : only logic change


if __name__ == '__main__':
    tree_root = BinaryTree.single_line_input(input_array(""))
    BinaryTree.display(tree_root)
    top_view_of_binary_tree(tree_root)
"""
                       1
                      / \
                     2   3
                    / \   \
                   4   5   6
                  /     \
                 7       8   

1 2 3 4 5 -1 6 7 -1 -1 8 -1 -1 -1 -1 -1 -1

Vertical Order 
7
4
2
1 5
3 8       <<  Note this order       Its correct now
6


Bottom View
7 4 2 5 8 6
"""

"""
       1
    /     \
   2       3
 /  \    /  \
4    5  6    7

1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1

Vertical Order
4
2
1 5 6
3
7

Bottom View
4 2 6 3 7
"""

"""
      10
    /      \
  20        30
 /   \    /    \
40   60  90    100

10 20 30 40 60 90 100 -1 -1 -1 -1 -1 -1 -1 -1 

Vertical Order
4
2
1 5 6
3
7

Bottom View
40 20 90 30 100
"""

"""
                      20
                    /    \
                  8       22
                /   \      \
              5      3      25
                    /  \      
                  10    14

20 8 22 5 3 -1 25 -1 -1 10 14 -1 -1 -1 -1 -1 -1

Vertical Order
5
8 10
20 3
22 14
25

Bottom View
5 10 3 14 25 
"""

"""
20 8 22 5 3 4 25 -1 -1 10 14 -1 -1 -1 -1 -1 -1 -1 -1 
                      20
                    /    \
                  8       22
                /   \    /   \
              5      3  4    25
                    / \      
                  10   14
Bottom View
5 10 4 14 25

Vertical Order
5
8 10
20 3 4
22 14
25
"""
