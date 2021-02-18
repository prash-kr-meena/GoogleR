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
    queue = deque()

    # enqueue - inserting at the Right
    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue.append(4)
    queue.append(5)
    queue.append(6)

    print(queue)  # Print
    print(queue[0])  # First Element / Top
    print(len(queue))  # Length
    print(len(queue) == 0)  # isEmpty

    # enqueue - Popping from Left
    queue.popleft()
    queue.popleft()

    print(queue)  # Print
    print(queue[0])  # First Element / Top
    print(len(queue))  # Length
    print(len(queue) == 0)  # isEmpty


if __name__ == '__main__':
    demo_queue_operation_using_deque()
    pass

"""
deque([1, 2, 3, 4, 5])
deque([3, 4, 5])
3
"""
