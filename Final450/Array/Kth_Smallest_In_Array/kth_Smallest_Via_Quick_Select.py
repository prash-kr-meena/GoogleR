from Final450.Searching_Sorting.Algorithms.Quick_Select import quick_select

"""
Average Case Time : O(n)      --> Using randomized partitioning, in our QuickSelect implementation
Worst case : O(n^2)

here, k is 1_indexed (Assumption)
"""


def kth_smallest__quick_select(A, k):
    return quick_select(A, left=0, right=len(A) - 1, k=k - 1)
    # But QuickSelect Method takes k as 0_indexed


if __name__ == '__main__':
    arr = [12, 3, 5, 7, 19]
    print(arr)
    print(kth_smallest__quick_select(arr, 2))

"""
[12, 3, 5, 7, 19]       - Random
[1, 2, 3, 4, 5, 6]      - Sorted
[9, 8, 7, 6, 5, 4]      - Reverse Sorted
[3, 3, 1, 8, 2, 1]      - Random with duplicates 
                          Wrong Result - doesn't handle duplicity
"""
