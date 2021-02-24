from Utils.Array import input_array

"""
 https://www.geeksforgeeks.org/to-find-smallest-and-second-smallest-element-in-an-array/
 Find the smallest and second smallest elements in an array

 Important part could be handling the corner cases, like handling the duplicates (even if you sort it)

 Approach 1 : sorting   O(n lg n)
 Approach 2 : 1 Pass    O(n)
"""


def find_first_second_and_third_smallest(nums):
    first_smallest = second_smallest = third_smallest = float("inf")

    for n in nums:
        if n < first_smallest:
            third_smallest = second_smallest
            second_smallest = first_smallest
            first_smallest = n
        elif n < second_smallest and n != first_smallest:  # to handle duplicate cases
            third_smallest = second_smallest
            second_smallest = n
        elif n < third_smallest and n != second_smallest and n != first_smallest:
            third_smallest = n

    return first_smallest, second_smallest, third_smallest


if __name__ == "__main__":
    array = input_array("List of integer numbers : ")
    first, second, third = find_first_second_and_third_smallest(array)
    print(first, second, third)

'''
------- Test cases ------- 

12 13 2 11 0 10
1 2 3 4 5 6 7       Imp
7 7 7 7 7 7 7       VVImp
3 2 2 1 1 2 3       v.v.v Imp   basically duplicate first and second smallest   
                    Need special condition otherwise both first and second will be same ie, 1, 1

'''
