from GenericTree import GenericTree
from Utils.Array import input_array


def print_nodes_at_particular_depth(root, k) -> None:
    # Two variables, so condition on both of them, and there could be a combination as well

    if root is None:  # Edge Case - Nothing to print
        return

    if k == 0:  # Reached the level
        print(root.data)
        return

    for child in root.children:
        print_nodes_at_particular_depth(child, k - 1)  # level keep on decreasing


if __name__ == '__main__':
    array = input_array()
    depth = int(input())
    tree_root = GenericTree.single_line_input(array)
    print_nodes_at_particular_depth(tree_root, depth)
    pass

"""
Note : Height of a tree, meaning Height is an attribute of the tree and not a particular node, where as

Depth of a node : is a property of the node, it is defined as the distance of that node from root



           10           -> 0 depth          0 distance away from the root, as it is the ROOT
      20   30   40      -> 1 depth          1 distance away from the root
    40 50               -> 2 depth          2 distance away from the root
"""

"""
Given a tree, and a value k, where  0 > k < height_of_the_tree
Print all the nodes, at depth k


10 3 20 30 40 2 40 50 0 0 0 0

           10           -> 0 depth
      20   30   40      -> 1 depth
    40 50               -> 2 depth


eg. if k=-1,    print NONE <as level can't be -ve>
    if k=0,     print 10
    if k=1,     print 20 30 40
    if k=2,     print 40 50
"""

"""

           10           -> 0 depth
      20   30   40      -> 1 depth
    40 50               -> 2 depth


10 3 20 30 40 2 40 50 0 0 0 0
0

10 3 20 30 40 2 40 50 0 0 0 0
1

10 3 20 30 40 2 40 50 0 0 0 0
2

10 3 20 30 40 2 40 50 0 0 0 0
-1

10 3 20 30 40 2 40 50 0 0 0 0
3
"""
