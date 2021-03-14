from Search_Sorting._Algorithms.Quick_Sort import partition
from Utils.Array import input_array

# https://www.geeksforgeeks.org/quickselect-algorithm/

"""
Note :  The partition process is exactly the same that is being used in the quicksort process,
        The difference bw the quick_sort & quick_select is the way they uses this pivot_index
"""

"""
finds the kth position (of the sorted array)  in a given unsorted array 
i.e this function can be used to find both kth largest and  kth smallest element in the array.
 
ASSUMPTION: All elements in arr[] are distinct 
            Then only you will be able to find the UNIQUE kth smallest or kth largest element

Behaviour with Duplicate Array Elements is : 
eg.     arr : [1 2 3 4 1 2 3 4 9 10]
then, the output will be
       k=0 =>  1
       k=1 =>  1
       k=2 =>  2
       k=3 =>  2
       k=4 =>  3
       k=5 =>  3
       k=6 =>  4
       k=7 =>  4
       k=8 =>  9
       k=9 =>  10

so if you require that
    k=0 => 1
and k=1 => 2    and not 1, ie you don't want duplicate element and just want unique elements for each k value
                then this algorithm will not work

But generally you don't have such requirement, so in that case it works
"""


# Assuming if k was 1_index_base, then this method you should pass k-1

# Find kth element, if the array would be sorted, Even though it is not sorted
def quick_select(A, left, right, k):  # kth is 0 indexed
    # Edge cases - Assumed checks
    if left > right:
        return Exception("Left can't be more then Right")
    if k < left or k > right:
        return Exception("k is not in the Left-Right range")
    if k < 0 or k >= len(A):
        return Exception("k is not in the range of the actual array")

    pivot_index = partition(A, left, right)

    if pivot_index == k:  # found   # No base case As its 100% that we will reach this case Notice
        return A[pivot_index]
    elif pivot_index < k:
        return quick_select(A, pivot_index + 1, right, k)
    else:
        return quick_select(A, left, pivot_index - 1, k)


if __name__ == "__main__":
    arr = input_array()
    for _ in range(len(arr)):  # put high no in range to see the edge cases
        num = quick_select(arr, left=0, right=len(arr) - 1, k=_)
        print(num, end=" ")

"""
[]
[3]
1 3 5 4 6 2             # random
12 3 5 7 4 19 26        # random
9 8 7 6 5 4 3 2 1       # reverse sorted
1 2 3 4 5 6 7 8 9 10    # sorted
1 2 3 4 1 2 3 4 9 10    # random duplicates -- CHECK IT OUT
"""
