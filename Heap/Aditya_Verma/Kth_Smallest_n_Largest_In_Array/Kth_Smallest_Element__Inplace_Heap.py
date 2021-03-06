from heapq import heapify, heappush, heappop

from Utils.Array import input_array

"""
https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1

Note : this problem can also be done by the quick select algorithm,
checkout package Kth_Smallest_n_Largest_In_Array in Array.Final450
"""

"""
As the problem is for kth Smallest : 
    1. if we are creating an external heap, of size k, then we would want a Max-Heap (opposite)
        which in case of primitives, we make by using -ve values with MIN-Heap
    2. if we are heapifying the given array only, ie the heap will be of size n, as the whole array is a heap now
        so in that case we should make the similar heap only, ie
            here we needed to find the kth min, so we should make a Min-Heap only,
            so we will be getting min element at top, and we can pop off k-1 elements and the kth element that we pop
            will be the one which we require


Assuming we can change the inbuilt array,
    1. Then instead of creating a max-heap and adding elements to them later on, each operation of log(n) so, O(n log n)
    2. We can heapify the given array, in O(n), ie building an heap of an array inplace is O(n)
        and then we can just pop off k elements having log (n) time, so O(k lg n)


Note : When you are creating a max heap in this way, pay attention if the values inside the array can be -ve or not?
        because if yes, then you might think this will impact as you will also be multiplying with -ve
        BUT if you think clearly it will not actually cause any problem,
            as when you will return you will also multiply be -ve
            and in the heap as well, it will have opposite property like all +ve --> -ve and similarly all -ve -> +ve
"""

"""
Time :    O(n) to heapify A,  popping k element from heap so O(k lg n)
          In total : O(n) + O(k lg n)

          O(n) + O(k lg n)   should be minimum when comparing  O(n) + O(k lg n) and O(n lg k)
          as, in O(n lg k)    it means O(n) time log k operation


Space :   O(1)
"""


def kth_smallest(A, k) -> int:
    if k >= len(A):  # Edge Case, k can't be more then array length
        return None

    heapify(A)  # Min_Heap, inplace heapify operation has O(n) time complexity,

    for i in range(1, k):  # pop till k-1 th elements,      k is 1 based index, that is why starting from 1
        heappop(A)

    return heappop(A)


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
