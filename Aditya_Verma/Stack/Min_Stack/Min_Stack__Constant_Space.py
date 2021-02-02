from Abstract_Data_Types.StackADT import StackADT
from Utils.Array import input_array


class MinStackADT:
    def __init__(self):
        self.main_stack = StackADT()
        self.min_element = None

    def push(self, element):
        if self.main_stack.is_empty():
            self.main_stack.push(element)
            self.min_element = element
        else:
            # Stack is not empty
            if element >= self.min_element:
                self.main_stack.push(element)
            else:
                value = 2 * element - self.min_element  # Notice : Formula
                self.main_stack.push(value)
                self.min_element = element

    def pop(self):
        if self.main_stack.is_empty():
            return None
        else:
            element = self.main_stack.pop()
            if element >= self.min_element:
                # The minimum element of the stack, is still the min_element
                return element
            else:
                self.min_element = 2 * self.min_element - element  # Notice : Formula
                return self.min_element  # the correct value of stack, and the correct minimum

    def size(self):
        return self.main_stack.size()

    def peek(self):
        # Basically similar to pop, just without the actual pop
        if self.main_stack.is_empty():
            return None
        else:
            element = self.main_stack.peek()  # Note : Only change from Pop() method
            if element >= self.min_element:
                # The minimum element of the stack, is still the min_element
                return element
            else:
                self.min_element = 2 * self.min_element - element  # Notice : Formula
                return self.min_element  # the correct value of stack, and the correct minimum

    def min(self):
        return self.min_element


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
