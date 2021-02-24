from Tree.CodingNinjas.GenericTree.GenericTree import GenericTree

from Utils.Array import input_array

"""
 Code : Number of nodes greater than x
 
 Given a tree and an integer x, find and return number of Nodes which are greater than x.
 
"""


def count_nodes_greater_then_x(root, x) -> int:
    if root is None:
        return 0

    count = 1 if root.data > x else 0  # handling the root

    # asking results from subtrees
    for child in root.children:
        count += count_nodes_greater_then_x(child, x)

    return count


if __name__ == '__main__':
    array = input_array("")
    value_x = array[0]
    del array[0]  # Removing the first element of the array, so remaining is the tree input
    tree_node = GenericTree.single_line_input(array)
    count = count_nodes_greater_then_x(tree_node, value_x)
    print(count)

"""
Single Line : First Integer denotes x and rest of the elements in level order form separated by space. Order is - 
Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element 

35 10 3 20 30 40 2 40 50 0 0 0 0
3       << OUTPUT

10 10 3 20 30 40 2 40 50 0 0 0 0
5       << OUTPUT
"""
