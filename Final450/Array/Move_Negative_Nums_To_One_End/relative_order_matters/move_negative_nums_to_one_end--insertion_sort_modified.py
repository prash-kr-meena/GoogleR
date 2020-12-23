# Time  : O(n2)
# Space : O(1) Constant space


"""
Ill be having 2 pointers here
one of them will move through the array looking for -ve numbers to operate on
and another will be pointing to the correct location where i can put the -ve elements, after i find them
    also this same location will denote the starting of the 1st +ve number in the array,
    --> as we will be going to move them forward

Finally when you find a -ve number, store it temporarily
do the swapping, to move all the +ve numbers forward by one step to, make place for the stored -ve number
then finally put that number in its correct position and move the pointer to store future -ve numbers

"""


def rearrange_via_modified_insertion_sort(A):
    # walking_index = 0
    index_to_place_nums = 0  # for placing -ve nums that i find

    for walking_index in range(0, len(A)):  # go through the array
        if A[walking_index] >= 0:  # +ve num, so move on
            continue

        # -ve num
        found_num = A[walking_index]  # temporary storage
        # move all the +ve numbers, before it forward by one step
        ptr = walking_index - 1
        while ptr >= index_to_place_nums:  # till it reaches the first +ve number
            A[ptr + 1] = A[ptr]
            ptr -= 1  # go back one step

        # reached, now put the -ve found, at its correct position
        A[index_to_place_nums] = found_num
        index_to_place_nums += 1  # updating, for the index of next -ve number


if __name__ == "__main__":
    # arr = [4, 3, 2, 1, 0, -1, -2, -3]
    arr = [12, 11, -13, -5, 6, -7, 5, -3, -6]
    rearrange_via_modified_insertion_sort(arr)
    print(arr)

"""
[12,11,-13,-5,6,-7,5,-3,-6]
[-1, 2, -3, 4, 5, 6, -7, 8, 9]
[2, 3, -1, -4, -6]                          # Reverse
[4, 3, 2, 1, 0, -1, -2, -3]                 # Reverse containing 0
"""
