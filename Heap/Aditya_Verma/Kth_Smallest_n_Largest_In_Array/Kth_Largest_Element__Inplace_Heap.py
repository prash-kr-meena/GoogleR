from heapq import heapify, heappush, heappop

"""
Need to find kth largest (maximum), We will be create a Max-Heap
and for that we will use -ve values for elements

Also as we will be doing inplace, so we will just modify A, for all -ve numbers
"""


def kth_smallest(A, k):
    if k >= len(A):  # Edge Case, k can't be more then array length
        return None

    A = [-e for e in A]  # making elements -ve  Notice
    heapify(A)

    for i in range(1, k):  # pop till k-1 th elements,      k is 1 based index, that is why starting from 1
        heappop(A)

    return -heappop(A)  # Notice


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input())
    print(kth_smallest(arr, k))
    print("sorted ", sorted(arr))

"""
N = 6
arr[] = 7 10 4 3 20 15
K = 3
3rd smallest element in the given array is 7.


6
7 10 4 3 20 15
3
===> Sorted : [3, 4, 7, 10, 15, 20]      so 3rd highest is 10


5
7 10 4 20 15
4
===> Sorted : [4, 7, 10, 15, 20]         here, 4 highest is 7


- Random with duplicates
6
3 3 1 8 2 1
1
==> 8

6
3 3 1 8 2 1
2
==> 3

6
3 3 1 8 2 1
3
==> 3


12 3 5 7 19      - Random
1 2 3 4 5 6      - Sorted
9 8 7 6 5 4      - Reverse Sorted
"""
