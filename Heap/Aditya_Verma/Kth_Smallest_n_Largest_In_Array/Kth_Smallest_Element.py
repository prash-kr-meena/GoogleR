from heapq import heapify, heappush, heappop

from Utils.Array import input_array

"""
https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1

Note : this problem can also be done by the quick select algorithm,
checkout package Kth_Smallest_n_Largest_In_Array in Array.Final450
"""

"""
As the problem is for kth Smallest : we need to make a Max-Heap
which in case of primitives, we make by using -ve values with MIN-Heap
"""

"""
Time :    here we are creating an empty heap, and having at most k elements in the heap,
              so popping will be O(lg k) and adding elements will be O(lg k)
          we are traversing the whole array so O(n) and either adding and/or  removing from the heap ie O(lg k)
          Total  : O(n lg k)

Space :   O(k) size of heap
"""


def kth_smallest(A, k) -> int:
    if k >= len(A):  # Edge Case, k can't be more then array length
        return None

    heap = []  # using min-heap as Max-Heap, so multiplying element with -ve
    heapify(heap)

    for element in A:
        heappush(heap, -element)  # Notice -ve
        if len(heap) > k:
            heappop(heap)

    return -heap[0]  # Top element of heap, ie the maximum (as Max-Heap) (Notice : -ve)


if __name__ == '__main__':
    n = int(input())
    arr = input_array()
    k = int(input())
    print(kth_smallest(arr, k))

"""
N = 6
arr[] = 7 10 4 3 20 15
K = 3
3rd smallest element in the given array is 7.


6
7 10 4 3 20 15
3
===> Sorted : [3, 4, 7, 10, 15, 20]      so 3rd smallest is 7


5
7 10 4 20 15
4
===> Sorted : [4, 7, 10, 15, 20]         here, 4 smallest is 15



- Random with duplicates
6
3 3 1 8 2 1
1
==> 1

6
3 3 1 8 2 1
2
==> 1

6
3 3 1 8 2 1
3
==> 2


12 3 5 7 19      - Random
1 2 3 4 5 6      - Sorted
9 8 7 6 5 4      - Reverse Sorted
"""
