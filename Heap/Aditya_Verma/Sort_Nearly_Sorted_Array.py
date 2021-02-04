from Utils.Array import print_array_inline
from heapq import heapify, heappush, heappop

"""
https://practice.geeksforgeeks.org/problems/nearly-sorted-algorithm/0
Sort a K Sorted Array       OR      Sort Nearly Sorted Array

# Not the typical, heap problem, Identifying its a heap problem is the key to solve this

As given, the correct value <according to the sorted order>
will be present within the k distance, either in left or right

The way to think about it, as we will be starting to fill the array from beginning, so basically we would have only
one direction, ie right

and as we are doing an ascending order sort, we will require min element on the top of our heap
hence we should have a min-heap  
"""


def sort_nearly_sorted_array(arr, k) -> None:
    sorted_arr = []  # we are not doing it inplace, but can be done with a little more effor

    heap = []  # Empty Min-Heap
    heapify(heap)

    for element in arr:
        heappush(heap, element)
        if len(heap) > k:
            curr = heappop(heap)  # this is the first element of the
            sorted_arr.append(curr)

    # empty the heap
    while len(heap) != 0:
        curr = heappop(heap)  # this is the first element of the
        sorted_arr.append(curr)

    print_array_inline(sorted_arr)


# input an list of space-separated integers <array>
def input_array() -> list:
    return list(map(int, input().strip().split()))


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, k = list(map(int, input().strip().split()))
        array = input_array()
        sort_nearly_sorted_array(array, k)

"""
2
3 3
2 1 3
6 3
2 6 3 12 56 8
"""
