# Approach 1: Sorting
# Time : O(n Log n)

# k is 1_indexed
def kth_smallest__sorting(A, k):
    A.sort()
    return A[k - 1]


if __name__ == '__main__':
    arr = [12, 3, 5, 7, 19]
    print(kth_smallest__sorting(arr, 2))

"""
[12, 3, 5, 7, 19]       - Random
[1, 2, 3, 4, 5, 6]      - Sorted
[9, 8, 7, 6, 5, 4]      - Reverse Sorted
[3, 3, 1, 8, 2, 1]      - Random with duplicates 
                          Wrong Result - doesn't handle duplicity
"""
