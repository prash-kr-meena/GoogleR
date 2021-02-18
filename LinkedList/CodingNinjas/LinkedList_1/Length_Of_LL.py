from sys import stdin
from Utils.LinkedList import get_linked_list_size, input_linked_list_with_end_value


def length(head):
    return get_linked_list_size(head)


if __name__ == '__main__':
    T = int(stdin.readline().rstrip())
    while T > 0:
        head_pointer = input_linked_list_with_end_value(-1)
        print(length(head_pointer))
        T -= 1

"""
1
3 4 5 2 6 1 9 -1

Output
7


2
10 76 39 -3 2 9 -23 9 -1
-1

Output
8
0

"""
