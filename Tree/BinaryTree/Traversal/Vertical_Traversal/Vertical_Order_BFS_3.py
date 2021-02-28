from collections import deque
from typing import Dict
from Tree.BinaryTree.BinaryTree import BinaryTree, BinaryTreeNode
from Tree.BinaryTree.Traversal.Vertical_Traversal.Vertical_Order_BFS_2 import finding_x_for_each_node__level_order
from Utils.Array import input_array, print_array_multiline, print_array_inline

"""
Set 3       <<<<<< Check that first
        
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
        
Here just to give the proof of concept, and to not make the logic complicated, i will just have another traversal
and find the min_hd and max_hd
>> The time complexity will still be similar ie O(n)

and we will be removing the sorted() method, which we use to get the sorted list of keys
"""


def vertical_order(root):
    x_table: Dict[int, list] = dict()  # map of number, list
    finding_x_for_each_node__level_order(root, x_table)

    # for x in sorted(x_table.keys()):                          <<<<<<<<<<<<< Removing sorting Notice
    #     print_array_inline(x_table[x])

    min_hd, max_hd = float("inf"), float("-inf")
    for key in x_table.keys():
        min_hd = min(min_hd, key)
        max_hd = max(max_hd, key)

    for i in range(min_hd, max_hd + 1):  # so that we include max_hd as well
        print_array_inline(x_table[i])


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
