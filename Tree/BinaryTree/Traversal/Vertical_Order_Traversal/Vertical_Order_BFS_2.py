from collections import deque
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
        Time Complexity : O(n lg n)
        Space : O(n)


>>> Below Implementation <<<<
set 3 : https://www.geeksforgeeks.org/print-a-binary-tree-in-vertical-order-set-3-using-level-order-traversal/  
        
        The above solution (Set 2) uses preorder traversal and Hashmap to store nodes according to horizontal distances.
        Since the above approach uses preorder traversal, 
        nodes in a vertical line may not be printed in the same order as they appear in the tree. 
        
        If we use level order traversal, we can make sure that if a node that comes below in the same vertical line,
          is printed after a node which comes above in the vertical line.
        
        Here we can resolve this problem, if instead of DFS we use BFS, 
        because we will complete all the nodes at top vertical_level first (basically depth)
        And with that we will account for the height of each of the node
        
Time Complexity : O( n log n)   Same as set 2
Space Complexity : O(n) + some_queue_space  ==> basically O(n) only


NOTE : we can actually, decrease the time-complexity from O(n lg n)  to O(n)
        just by using two variable min_hd, max_hd (ie, minimum_horizontal_distance, maximum_horizontal_distance)
        Two ways to implement
            1. we can find out these min_hd, max_hd while doing the BFS and DFS itself
            2. or we could later on traverse the map and find out these min_hd, max_hd
        
        It is sure that in the range of this min_hd and max_hd there will be at least onve node at that vertical_level
        (In general there would always ALWAYS be, at-least be one node in any vertical_level or horizontal_level)
        once we have these values, now we can just loop from min_hd to max_hd and get the values from the regular map
"""

"""
The idea is to do a simple BFS approach,
and while traversing in a BFS way, for each node maintain its horizontal_distance ie, x coordinate
x = horizontal distance :   we assume root to start at 0, 
                            so, its left_child will be 1 unit left ie -1 
                            and right_child will be 1 unit right ie +1  

If the two nodes have same horizontal distance, then it means that they are on the same-vertical-line
like how we, can say, if two nodes have depth (vertical_distance) then the are at same-horizontal-line

We would have to have a track of the horizontal_distance, 
so we would require to create a pair for each node and its horizontal_distance, 
so with respect to that we can update the horizontal_distance for the childrens as well 
"""


def finding_x_for_each_node__level_order(root, x_table: Dict[int, list]) -> None:
    queue = deque()
    queue.append((root, 0))  # horizontal_distance for root is 0

    while len(queue) != 0:
        curr_root, curr_horizontal_distance = queue.popleft()

        # Process Node ->  we need to store x (Horizontal Distance) in the map ie dictionary
        if x_table.get(curr_horizontal_distance) is None:
            # create the mapping
            x_table[curr_horizontal_distance] = list()  # new empty list
            x_table[curr_horizontal_distance].append(curr_root.data)  # append this vertical distance to the list
        else:
            # mapping already present
            x_table[curr_horizontal_distance].append(curr_root.data)  # append this vertical distance to the list

        if curr_root.left is not None:
            queue.append((curr_root.left, curr_horizontal_distance - 1))  # decrementing

        if curr_root.right is not None:
            queue.append((curr_root.right, curr_horizontal_distance + 1))  # incrementing


def vertical_order(root):
    x_table: Dict[int, list] = dict()  # map of number, list
    finding_x_for_each_node__level_order(root, x_table)

    for x in sorted(x_table.keys()):
        print_array_inline(x_table[x])


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
3 8       <<  Note this order       Its correct now
6
"""

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


"""
