from heapq import heapify, heappush, heappop

"""
https://practice.geeksforgeeks.org/problems/k-largest-elements3736/1

This problem can be solve using sorting, but that will take O(n lg n)

With heap we can do it in O(n lg k)
"""


# As the problem is for kth Largest : we need to make a Min-heap
def k_largest(A, k) -> list:
    heap = []  # using a min-heap
    heapify(heap)

    for element in A:
        heappush(heap, element)
        if len(heap) > k:
            heappop(heap)

    # Only sort these K elements, to get Descending Order
    heap.sort(reverse=True)
    return heap  # Top element of heap, ie the maximum


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input())
    print(k_largest(arr, k))

"""
5
12 5 787 1 23
2

7
1 23 12 9 30 2 50
3

5
7 10 4 3 20 15
3

"""
