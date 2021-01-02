# For using stack in python
# https://www.geeksforgeeks.org/stack-in-python/
# https://www.youtube.com/watch?v=zwb3GmNAtFk&ab_channel=codebasics   << NOTE good resource

from collections import deque


# Stack_ADT_Using_Deque
class StackADT:

    # stack = deque()       initializing a deque, named stack

    def __init__(self, list_of_elements=None):
        if list_of_elements is None:
            self.stack = deque()  # Initialize an Empty Stack
        else:
            self.stack = deque()  # Stack with elements
            for element in list_of_elements:
                self.stack.append(element)

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]  # Returning last element

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def __str__(self) -> str:
        return self.stack.__str__()  # OR  return str(self.stack)

    def print(self) -> None:
        self.print_recursively()
        print()

        """
        Printing Iteratively
        If we did it iteratively we would require to get one extra stack and had to do iterations
        1. In 1st iteration we would pop each element and print them one by one, in LIFO pattern
            and also keep them pushing into another stack
        2. In 2nd iteration, we would pop elements from the 2nd stack and push it back to the original stack
        """

    def print_recursively(self):
        """
        Printing recursively - From Top to Bottom - Note : the logic
        """
        # Base Case
        if self.size() == 0:
            return

        top_element = self.pop()
        print(top_element, end=" ")
        self.print_recursively()  # With one less element
        self.push(top_element)

        pass


def stack_demonstration(stack: StackADT):
    # elements
    print(stack)

    # pushing elements
    stack.push(5)
    stack.push(1)
    stack.push(0)
    stack.push(2)
    print(stack)

    # popping elements
    print(stack.pop(), "< Popped")
    print(stack.pop(), "< Popped")

    # Size of the stack
    print(stack.size(), "<- Stack Size")

    # Print Elements
    stack.print()


if __name__ == "__main__":
    stack = StackADT()
    stack_demonstration(stack)

    another_stack = StackADT([1, 2, 3, 4])
    another_stack.print()
