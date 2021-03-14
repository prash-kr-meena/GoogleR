from Utils.Array import input_array

"""
Important Question

As of now we have stabilised, that to find the no_of_times_the_array_is_rotated
we basically need to  find the index of the smallest element in the rotated array

Now if we do that in the in a linear search : it will have O(n) time complexity
But we can do it in O(lg n) using binary search
"""

"""
Assumptions and Clarifications:
We are looking at Increasingly Ordered sorted elements only here        [smaller -----------------> Higher]

When an array is rotated, not matter in which direction, clockwise or anti-clockwise
The smaller element will come after some elements, basically the structure will be something like this
[ smaller------------->large  <<smallest_element>>  -------> larger ] 

so the logic for finding the index of the smallest element remains the same, no matter what

But when you want to count the number of rotation, now that actually depends on the way you are rotating
* Clock-Wise       (Right) Rotation  
    =>  ie, you put the right most element and push it in the beginning
        So, in this case the rotation_count = index_of_min_element

* Anti-Clock-Wise  (Left)  Rotation  
    =>  ie, you put the left most element and push it in the ending
        So, in this case the rotation_count = (length - index_of_min_element) % length


NOTE : This code is applicable with a condition that there are  ---- NO REPEATED VALUES -----
       It is a standard interview problem (search_element_in_rotated_sorted_array )you can find out on leetcode
"""


# Handling the case then the array is not rotated, ie rotation = 0
def find_no_of_times_sorted_array_is_rotated(arr) -> int:
    if arr is None or len(arr) == 0:
        return 0

    n = len(arr)
    left = 0
    right = n - 1

    while left <= right:
        if arr[left] <= arr[right]:  # Array is already sorted
            return left

        mid = (left + right) // 2
        next = (mid + 1) % n
        prev = (mid + n - 1) % n

        if arr[mid] <= arr[prev] and arr[mid] <= arr[next]:
            return mid
        elif arr[left] <= arr[mid]:  # Left array is sorted, so go in Right (un-sorted) array
            left = mid + 1
        elif arr[mid] <= arr[right]:  # Right array is sorted, so go in Left (un-sorted) array
            right = mid - 1

    return -1


if __name__ == '__main__':
    array = input_array()
    print(find_no_of_times_sorted_array_is_rotated(array))

"""
15 18 2 3 6 12
2 << Output

7 9 11 12 5
4 << Output

7 9 11 12 15
0 << Output

[]     ## Just Hit Enter
0 << Output


1     ## Array with single element
0 << Output
"""
