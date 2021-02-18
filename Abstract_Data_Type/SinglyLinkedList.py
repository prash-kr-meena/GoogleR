from Utils.Array import input_array


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None  # head, tail is of type Node
        self.tail = None

    def input_linked_list(self) -> None:
        """
        In our case, we do not need -1 to stop taking input
        """
        linked_list_data = input_array()

        temporary_node = Node(-9999999)
        self.head = self.tail = temporary_node  # To get rid off null check on head, in the loop

        # tail : will work as the moving_pointer
        for data in linked_list_data:
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = self.tail.next

        self.head = self.head.next  # passing over the temporary_node

    def print_linked_list(self) -> None:
        pointer = self.head
        linked_list_data___in_str_format = []
        while pointer is not None:
            linked_list_data___in_str_format.append(str(pointer.data))
            pointer = pointer.next

        print(" -> ".join(linked_list_data___in_str_format))

    def get_linked_list_size(self) -> int:
        pointer = self.head
        length = 0
        while pointer is not None:
            length += 1
            pointer = pointer.next

        return length

    def insert_at_beginning(self):
        # Todo
        pass

    def insert_at_end(self):
        # Todo
        pass

    def delete_from_beginning(self):
        # Todo
        pass

    def delete_from_end(self):
        # Todo
        pass

    def check_if_palindrome(self):
        # Todo
        pass

    def reverse(self):
        # Todo
        pass


if __name__ == '__main__':
    linkedList = SinglyLinkedList()
    linkedList.input_linked_list()
    linkedList.print_linked_list()
    print(linkedList.get_linked_list_size())

"""
1 2 3 4 5 6 5 4 3 2 1
"""
