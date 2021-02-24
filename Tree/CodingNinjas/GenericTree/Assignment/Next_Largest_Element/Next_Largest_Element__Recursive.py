from Tree.CodingNinjas.GenericTree.GenericTree import GenericTree


def next_largest_element(root, n) -> int:

    pass


if __name__ == '__main__':
    n = int(input("num :"))
    tree_root = GenericTree.single_line_input(input(""))
    next_largest = next_largest_element(tree_root, n)
    print(next_largest)

"""
18
10 3 20 30 40 2 40 50 0 0 0 0 


21
10 3 20 30 40 2 40 50 0 0 0 0 

"""
