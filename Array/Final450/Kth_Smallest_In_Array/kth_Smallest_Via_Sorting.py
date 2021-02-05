from Utils.Array import input_array


# Approach 1: Sorting
# Time : O(n Log n)

# k is 1_indexed (Assumption)
def kth_smallest__sorting(A, k):
    A.sort()  # This is inplace sort, sorted(A) will be out-of-place
    return A[k - 1]


if __name__ == '__main__':
    arr = input_array()
    k = int(input("k : "))
    print(kth_smallest__sorting(arr, k))

"""
12 3 5 7 19      - Random
1 2 3 4 5 6      - Sorted
9 8 7 6 5 4      - Reverse Sorted
3 3 1 8 2 1      - Random with duplicates 
                   Notice : Wrong Result - doesn't handle duplicity
"""
