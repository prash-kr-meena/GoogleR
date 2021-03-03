"""
Merge two sorted Arrays without extra space
Arrays Google Doc   : https://docs.google.com/document/d/1NUoBX8WzYYkKRQdIxuN_K_406NtmBm5vfL0AzEceaHQ/edit#heading=h.84llj8puqlhz
"""
from Utils.Array import input_array, print_array_inline

"""
Lower Level :  Merge_2_Sorted_Arrays.py


Striver Video : https://www.youtube.com/watch?v=hVl2b3bLzBw&ab_channel=takeUforward
techiedelight : https://www.techiedelight.com/inplace-merge-two-sorted-arrays/

Brute Force : 
here we are implementing the brute force approach and not the more optimized GAP algorithm

So observe that, the first element of the second array ie, B 
has to be greater then that of the (all elements) last element of A

so we take reference to the first element of B, ie B[0] and with respect to that we will sort all A elements


Time  : O(n * m)
Space : O(1)  
"""


def merge_2_sorted_arrays_without_space(A, B):
    n = len(A)
    m = len(B)

    ptr_a = 0

    while ptr_a != n:
        if A[ptr_a] <= B[0]:
            ptr_a += 1
        else:
            # B[0] is smaller then current A's element
            A[ptr_a], B[0] = B[0], A[ptr_a]  # swap them

            # Sort B, by putting B[0] at its correct position in B, to maintain the sorted order of B.
            # Note: B[1 ... n-1] is already sorted
            for i in range(1, m):
                if B[i - 1] > B[i]:
                    B[i - 1], B[i] = B[i], B[i - 1]  # swap

            # sort the array B, as it might be distorted :
            # Using Insertion sort (as it will take O(n) only)       --> as the array is partially sorted only
            # Note : You can't just call insertion_sort algorithm, because that will assume all the elements un-sorted
            #  and will apply sorting on all of them, which will result in O(n^2) time,
            #  Instead ::: we should just sort this element only by putting it onto the correct location --> O(n) time


if __name__ == "__main__":
    arrA = input_array()
    arrB = input_array()
    merge_2_sorted_arrays_without_space(arrA, arrB)

    print_array_inline(arrA)
    print_array_inline(arrB)

"""
arrA = 1  3  5  7  9
arrB = 0  2  4  6  8

arrA =  1  1  5  5  10
arrB = -1  0  0  1  1  8

X = 1 4 7 8 10
Y = 2 3 9
"""
