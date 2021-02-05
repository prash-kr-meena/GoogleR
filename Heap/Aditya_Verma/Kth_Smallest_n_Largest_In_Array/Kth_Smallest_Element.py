from heapq import heapify, heappush, heappop

"""
https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1

Note : this problem can also be done by the quick select algorithm,
checkout package Kth_Smallest_n_Largest_In_Array in Array.Final450
"""


# As the problem is for kth Smallest : we need to make a Max-Heap
# which in case of primitives, we make by using -ve values with MIN-Heap
def kth_smallest(A, k):
    if k >= len(A):  # Edge Case, k can't be more then array length
        return None

    heap = []  # using min-heap as Max-Heap
    heapify(heap)

    for element in A:
        heappush(heap, -element)  # Notice -ve
        if len(heap) > k:
            heappop(heap)

    # print(heap)
    return -heap[0]  # Top element of heap, ie the maximum (as Max-Heap) (Notice : -ve)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
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

6
3 3 1 8 2 1
2

6
3 3 1 8 2 1
3



12 3 5 7 19      - Random
1 2 3 4 5 6      - Sorted
9 8 7 6 5 4      - Reverse Sorted

"""
