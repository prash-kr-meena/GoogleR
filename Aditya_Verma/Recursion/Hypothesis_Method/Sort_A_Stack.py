# For using stack in python
# https://www.geeksforgeeks.org/stack-in-python/
# https://www.youtube.com/watch?v=zwb3GmNAtFk&ab_channel=codebasics   << NOTE good resource


from Abstract_Data_Types.StackADT import StackADT


def insert_into_sorted_stack(stack, element) -> None:
    # Edge case
    if stack is None:
        raise ValueError("Invalid Stack")

    # Base case
    if stack.size() == 0 or stack.peek() <= element:
        stack.push(element)
        return

    top_element = stack.pop()
    insert_into_sorted_stack(stack, element)  # Hypothesis
    stack.push(top_element)

    # No induction Step


def sort_stack(stack) -> None:
    # Edge case
    if stack is None:
        raise ValueError("Invalid Stack")

    # Base case
    if stack.size() == 0 or stack.size() == 1:  # Already sorted
        return

    top_element = stack.pop()
    sort_stack(stack)  # stack has been reduced
    insert_into_sorted_stack(stack, top_element)


if __name__ == "__main__":
    s = StackADT([5, 1, 0, 2])
    s.print()  # unsorted stack
    sort_stack(s)
    s.print()  # sorted stack
