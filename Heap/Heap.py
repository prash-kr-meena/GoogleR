from heapq import heapify, heappush, heappop

from Utils.Array import input_array

"""
------- This is for Primitive types ------- 

This is by default a Min-Heap Implementation
To use it as a Max-heap, you need to use -ve values
"""


class Heap:

    def __init__(self, array=[]):
        # If array is not provided then will create an empty heap
        # Otherwise, will create a heap by heapify-ing the given array
        self.heap = array
        heapify(self.heap)

    def push(self, item):
        heappush(self.heap, item)

    def pop(self):
        if len(self.heap) == 0:
            print("Heap is empty - Can't pop")
        else:
            return heappop(self.heap)

    def peek(self):
        if len(self.heap) == 0:
            print("Heap is empty")
        else:
            return self.heap[0]

    def size(self):
        return len(self.heap)


def min_heap_demo(arr):
    min_heap = Heap(arr)

    print("Head value of heap : ", min_heap.peek())

    print("The heap elements : ", end="")
    while min_heap.size() != 0:
        print(min_heap.pop(), end=" ")
    print("\n")


def max_heap_demo(arr):
    arr = [-e for e in arr]  # Negate the elements
    print(arr)
    min_heap = Heap(arr)

    print("Head value of heap : ", -min_heap.peek())  # Negate, to make it +ve

    print("The heap elements : ")
    while min_heap.size() != 0:
        print(-min_heap.pop(), end=" ")  # Negate, to make it +ve
    print("\n")
    pass


if __name__ == '__main__':
    array = input_array()

    arr1 = [e for e in array]  # copy 1
    min_heap_demo(arr1)

    arr2 = [e for e in array]  # copy 2
    max_heap_demo(arr2)

"""
50 30 30 2 1
"""
