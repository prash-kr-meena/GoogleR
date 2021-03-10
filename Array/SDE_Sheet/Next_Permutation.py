from Utils.Array import input_array, reverse_array_inplace

"""
Submitted on LeetCode : https://leetcode.com/problems/next-permutation/

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such an arrangement is not possible, it must rearrange it as the lowest possible order ie, sorted in ascending order.
"""

"""
What if we have duplicates in the number - Note we need to pick the last element which is just greater
eg. [2, 3, 1, 3, 3]

so our element_index = 2        ie value = 1
now we go from index 3 to last
we see there are two values of 3, so we need to choose the last one
"""

"""
There is a BruteForce solution as well, which is of O(n!) time complexity

While this is an optimized solution 
Time  : O(n)
Space : O(1)
"""


# Find the next permutation, and if no permutation exists then sort the array in increasing order
def next_permutation(arr) -> None:  # doing inplace
    n = len(arr)

    # go from Right -> Left
    element_index = None

    for i in range(n - 1, 0, -1):  # idx 0 is excluded, so i will go to index n-1 to 1      , Reverse Direction
        if arr[i - 1] < arr[i]:  # find a number where the decreasing sequence breaks
            element_index = i - 1
            break

    if element_index is None:
        # whole array is in decreasing order, ie no other permutation exists    ==> return sorted array
        arr.sort()
        return

    # Breaking sequence found
    # Now to the right, and find the element that is just greater then the element at arr[i-1]
    j = element_index + 1  # as i-1 + 1  ==> i     starting from the next of arr[i+1]
    just_greater_index = j
    while j < n:
        if arr[j] > arr[element_index] and arr[j] <= arr[just_greater_index]:  # choosing the last just greater element
            just_greater_index = j
        j += 1

    # swap elements at element_index ie [i-1] and just_greater_index
    arr[element_index], arr[just_greater_index] = arr[just_greater_index], arr[element_index]

    # now revers it from element_index to the last index
    reverse_array_inplace(arr, element_index + 1, n - 1)


if __name__ == '__main__':
    array = input_array()
    print(array, end=" ")
    next_permutation(array)
    print(array)
"""
5 4 3 2 1

1 2 3 4 5

8 4 6 5 4 3 2

2 3 1 3 3
"""
