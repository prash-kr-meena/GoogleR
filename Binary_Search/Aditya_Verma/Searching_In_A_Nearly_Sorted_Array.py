from Utils.Array import input_array

"""
In this question statement : The nearly sorted array thing, is very similar to one of the questions we did in heap
Problem Name : Sort nearly sorted array        or         Sort a K Sorted Array           check in notion as well

One thing to remember is the difference bw [nearly_sorted / k_sorted]  and sorted_rotated_array  << Note
"""

"""
 ^^^^^^  Important Question  ^^^^^^ 
We will modify the standard binary search implementation a little bit
"""


# nearly_sorted   vs    sorted_rotated_array
def find_key_in_nearly_sorted_array(A, key) -> int:
    n = len(A)
    left = 0
    right = n - 1

    while left <= right:
        mid = left + (right - left) // 2

        prev = (mid + n - 1) % n
        next = (mid + 1) % n

        # comparing with mid, mid-1 and mid+1
        if A[mid] == key:
            return mid
        elif A[prev] == key:
            return prev
        elif A[next] == key:
            return next
        # mid is not in any of the near 3 indexes

        elif A[mid] < key:  # key present in the right half
            left = mid + 2
        else:  # A[mid] > key:   # key present in the right half
            right = mid - 2

    return -1


if __name__ == '__main__':
    array = input_array()
    target = int(input())
    index = find_key_in_nearly_sorted_array(array, target)
    print("index ", index)

"""
10 30 40 20 50 80 70
40
2   << Output:    Output is index of 40 in given array

10 30 40 20 50 80 70
90
-1  << Output       -1 is returned to indicate element is not present


10 30 40 20 50 80 70
10
0   << Output

10 30 40 20 50 80 70
70
0   << Output

10 30 40 20 50 80 70
20
3   << Output
"""
