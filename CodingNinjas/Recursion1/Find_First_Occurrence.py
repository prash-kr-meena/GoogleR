from sys import setrecursionlimit

'''
basically an extension of the Check_Number_Presence_In_UnSorted_Array.py Question
But here we will not be doing backward implementation, because we are concerned with the first occurrence of it

Its not that it can't be done,  but it will be Inefficient to do in backward direction
because even after finding a match(occurrence) we require to look into the backward array,
if any value is present or not because if yes then that will be the first occurrence

Time  : O(n)   In Worst Case - Checking every element
Space : O(n)

BOTH implementations are indexed based
'''


def find_first_occurrence__forward(nums, key, index) -> int:
    # Base Case
    if index >= len(nums):
        return -1  # Exhausted the array

    # Induction
    if nums[index] == key:  # Here we don't traverse full array if we find the match initially
        return index

    # Hypothesis
    return find_first_occurrence__forward(nums, key, index + 1)


def find_index_of_first_occurrence__forward(nums, key, ) -> int:
    return find_first_occurrence__forward(nums, key, 0)


#  ------------------- Little UnEfficient -------------------

def find_first_occurrence__backward(nums, key, n) -> int:
    # Base Case
    if n == 0:
        return -1  # Exhausted the array

    # Hypothesis
    occurrence_index_smaller_array = find_first_occurrence__backward(nums, key, n - 1)

    # Induction
    if occurrence_index_smaller_array != -1:  # ie we did find occurrence in smaller array
        return occurrence_index_smaller_array
    elif nums[n - 1] == key:  # last element is similar to key
        return n - 1
    else:
        return -1


def find_index_of_first_occurrence__backward(nums, key) -> int:
    return find_first_occurrence__backward(nums, key, len(nums))


if __name__ == "__main__":
    setrecursionlimit(11000)
    n = int(input())
    arr = list(int(i) for i in input().strip().split(' '))
    x = int(input())

    print(find_index_of_first_occurrence__forward(arr, x))
    print(find_index_of_first_occurrence__backward(arr, x))

'''
4
9 8 10 8
8
'''
