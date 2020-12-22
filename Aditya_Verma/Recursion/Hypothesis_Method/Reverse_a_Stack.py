from Abstract_Data_Types.StackADT import StackADT

'''
reverse stack - Recursively (with and without aux space), Iteratively
'''


def reverse_stack__Recursive__Auxilary_space(stack) -> None:
    """
        This is inplace
    """

    # Base Case
    if stack.size() == 0 or stack.size() == 1:  # Already Reversed
        return

    # Hypothesis Step
    top_element = stack.pop()
    reverse_stack__Recursive__Auxilary_space(stack)  # Stack has been reversed

    # Induction Step
    another_stack = StackADT()
    while not stack.is_empty():
        another_stack.push(stack.pop())

    stack.push(top_element)

    while not another_stack.is_empty():
        stack.push(another_stack.pop())  # pushing back into the original stack


def reverse_stack__Iterative__Auxilary_space(stack) -> StackADT:
    """
    This is not inplace
    """
    reversed_stack = StackADT()
    while not stack.is_empty():
        reversed_stack.push(stack.pop())

    return reversed_stack


def insert_into_bottom(stack, element) -> None:
    # Base Case
    if stack.is_empty():  # stack.size() == 0
        stack.push(element)
        return

    # Hypothesis
    top_element = stack.pop()
    insert_into_bottom(stack, element)

    # Induction step
    stack.push(top_element)


def reverse_stack__Recursive__Constant_Aux_Space(stack):
    """
    There is space used in recursion stack, But here the auxilary space for the problem is Constant O(1)
    The code is same, here in the induction step we are calling another recursive method for inserting into bottom

    This is also inplace
    """

    # Base Case
    if stack.size() == 0 or stack.size() == 1:  # Already Reversed
        return

    # Hypothesis Step
    top_element = stack.pop()
    reverse_stack__Recursive__Auxilary_space(stack)  # Stack has been reversed

    # Induction Step
    insert_into_bottom(stack, top_element)


if __name__ == "__main__":
    # s = StackADT([2, 4, 6, 0, 1])
    s = StackADT([9, 1, 2, 8, 4, 3])
    s.print()

    reverse_stack__Recursive__Constant_Aux_Space(s)
    s.print()

    reverse_stack__Recursive__Auxilary_space(s)
    s.print()

    reversed_stack = reverse_stack__Iterative__Auxilary_space(s)
    reversed_stack.print()
