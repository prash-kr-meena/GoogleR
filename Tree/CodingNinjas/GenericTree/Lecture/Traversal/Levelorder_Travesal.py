from Tree.CodingNinjas.GenericTree.GenericTree import GenericTree
from Utils.Array import input_array

if __name__ == '__main__':
    array = input_array()
    tree_root = GenericTree.single_line_input(array)
    GenericTree.print_level_order(tree_root)

"""
10 3 20 30 40 2 40 50 0 0 0 0

           10
      20   30   40
    40 50
"""
