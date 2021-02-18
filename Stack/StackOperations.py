from collections import deque

"""
Operations
* Enqueue
* Dequeue
* Peek (first element)
* Size
* IsEmpty
* Print
"""


def demo_queue_operation_using_deque():
    stack = deque()

    # enqueue - inserting at the Right
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    stack.append(5)
    stack.append(6)

    print(stack)  # Print
    print(stack[-1])  # Last Element / Top
    print(len(stack))  # Length
    print(len(stack) == 0)  # isEmpty

    # enqueue - Popping from Right
    stack.pop()
    stack.pop()

    print(stack)  # Print
    print(stack[0])  # First Element / Top
    print(len(stack))  # Length
    print(len(stack) == 0)  # isEmpty


if __name__ == '__main__':
    demo_queue_operation_using_deque()
    pass

"""
deque([1, 2, 3, 4, 5])
deque([3, 4, 5])
3
"""
