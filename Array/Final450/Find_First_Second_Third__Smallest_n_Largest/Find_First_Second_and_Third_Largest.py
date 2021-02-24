from Utils.Array import input_array

"""
 Important part could be handling the corner cases, like handling the duplicates (even if you sort it)

 Approach 1 : sorting   O(n lg n)
 Approach 2 : 1 Pass    O(n)
"""


def find_first_second_and_third_largest(nums):
    first_largest = second_largest = third_largest = float("-inf")

    for n in nums:
        if n > first_largest:
            third_largest = second_largest
            second_largest = first_largest
            first_largest = n
        elif n > second_largest and n != first_largest:  # to handle duplicate cases
            third_largest = second_largest
            second_largest = n
        elif n > third_largest and n != second_largest and n != first_largest:
            third_largest = n

    return first_largest, second_largest, third_largest


if __name__ == "__main__":
    array = input_array("List of integer numbers : ")
    first, second, third = find_first_second_and_third_largest(array)
    print(first, second, third)

'''
------- Test cases ------- 

12 13 2 11 0 10
1 2 3 4 5 6 7       Imp
7 7 7 7 7 7 7       VVImp
3 2 2 1 1 2 3       v.v.v Imp   basically duplicate first and second smallest   
                    Need special condition otherwise both first and second will be same ie, 1, 1

'''
