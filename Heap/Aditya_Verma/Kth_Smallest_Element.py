from heapq import heapify, heappush, heappop

"""
https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1

Note : this problem can also be done by the quick select algorithm
"""


# As the problem is for kth Smallest : we need to make a Max-heap
# which in case of primitives, we make by using -ve values with MIN-Heap
def kth_smallest(A, left, right, k):
    heap = []  # using a min-heap
    heapify(heap)

    for element in A:
        heappush(heap, -element)  # Notice -ve
        if len(heap) > k:
            heappop(heap)

    # print(heap)
    return -heap[0]  # Top element of heap, ie the maximum  (Notice : -ve)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input())
    print(kth_smallest(arr, 0, n - 1, k))

"""
N = 6
arr[] = 7 10 4 3 20 15
K = 3
3rd smallest element in the given array is 7.


6
7 10 4 3 20 15
3

5
7 10 4 20 15
4
"""
