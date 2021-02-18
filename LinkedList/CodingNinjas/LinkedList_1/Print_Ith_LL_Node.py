from sys import stdin
from Utils.LinkedList import input_linked_list_with_end_value


def print_ith_node(head, i):
    j = 0
    while head is not None:
        if j == i:
            print(head.data)
            return

        head = head.next
        j += 1


# Your code goes here


if __name__ == '__main__':
    T = int(stdin.readline().rstrip())
    while T > 0:
        head_pointer = input_linked_list_with_end_value(-1)
        ith = int(input())
        print_ith_node(head_pointer, ith)
        T -= 1
