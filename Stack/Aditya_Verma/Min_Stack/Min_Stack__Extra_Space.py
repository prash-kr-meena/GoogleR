from Abstract_Data_Type.StackADT import StackADT
from Utils.Array import input_array


class MinStackADT:
    def __init__(self):
        self.main_stack = StackADT()
        self.supporting_stack = StackADT()  # To maintain the corresponding minimum values

    def push(self, element):
        # Push into both the main_stack and the supporting_stacl
        self.main_stack.push(element)

        if self.supporting_stack.is_empty():
            self.supporting_stack.push(element)
        else:
            # supporting stack is not empty, find the minimum and push it to the supporting_stack
            minimum = min(element, self.supporting_stack.peek())
            self.supporting_stack.push(minimum)

    def pop(self):
        if self.main_stack.is_empty():
            return None
        else:
            # Pop from both the main_stack and the supporting_stacl
            self.supporting_stack.pop()
            return self.main_stack.pop()

    def size(self):
        # Size of both the stack will be similar here
        return self.main_stack.size()

    def peek(self):
        if self.main_stack.is_empty():
            return None
        else:
            return self.main_stack.peek()

    def min(self):
        # Will give minimum using the supporting stack
        if self.supporting_stack.is_empty():
            return None
        else:
            return self.supporting_stack.peek()


def demonstrate_min_stack():
    minstack = MinStackADT()

    numbers = input_array()
    for num in numbers:
        minstack.push(num)

    while minstack.size() != 0:
        print(minstack.min())
        minstack.pop()


if __name__ == '__main__':
    demonstrate_min_stack()

"""
18 19 29 15 16
"""
