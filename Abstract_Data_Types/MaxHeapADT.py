class MaxHeapADT:
    def __init__(self):
        self.heap = list()

    #  ---- Public methods  ----
    def push(self, element):
        # add to the end and heapify_up
        self.heap.append(element)
        self._heapify_up(self.size() - 1)
        print(self.heap)

    def pop(self):
        if self.size() == 0:  # If heap is empty
            return None
        else:
            # Swap top element with the last element of the heap (list) and
            # Delete the last element
            # heapify down the top element
            # Return the top element
            popped = self.heap[0]
            self._swap(0, self.size() - 1)
            del self.heap[self.size() - 1]  # delete last element
            self._heapify_down(0)
            return popped

    def peek(self):
        if self.size() == 0:  # If heap is empty
            return None
        else:
            return self.heap[0]  # Top element

    def size(self):
        return len(self.heap)

    # ---- Private Method ----
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, child_index):
        if child_index == 0:  # This is the top most element, and cant be bubbled up more
            return

        parent_index = (child_index - 1) // 2  # (i-1)/2        Notice : Integer Division

        # Bubble it up : if not at correct position
        if self.heap[child_index] > self.heap[parent_index]:
            # swap them and heapify the parent now
            self._swap(child_index, parent_index)
            self._heapify_up(parent_index)

    def _heapify_down(self, parent_index):
        # (2*i)+1 and (2*i)+2
        right_child_index = 2 * parent_index + 1
        left_child_index = 2 * parent_index + 2

        index_of_largest_element = parent_index
        if left_child_index < self.size() and self.heap[left_child_index] > self.heap[index_of_largest_element]:
            index_of_largest_element = left_child_index

        elif right_child_index < self.size() and self.heap[right_child_index] > self.heap[index_of_largest_element]:
            index_of_largest_element = right_child_index

        if index_of_largest_element != parent_index:
            self._swap(index_of_largest_element, parent_index)
            self._heapify_down(parent_index)

    def __str__(self):
        print(self.heap)


def max_heap_demonstration():
    max_heap = MaxHeapADT()
    for i in range(9):
        max_heap.push(i)

    while max_heap.size() != 0:
        print(max_heap.pop())


if __name__ == '__main__':
    max_heap_demonstration()
