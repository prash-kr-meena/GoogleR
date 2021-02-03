from Utils.Array import input_array

"""
 https://www.geeksforgeeks.org/to-find-smallest-and-second-smallest-element-in-an-array/
 Find the smallest and second smallest elements in an array

 Important part could be handling the corner cases, like handling the duplicates (even if you sort it)

 Approach 1 : sorting   O(n lg n)
 Approach 2 : 1 Pass    O(n)
"""


def find_first_and_second_smallest(nums):
    first_smallest = second_smallest = float("inf")

    for n in nums:
        if n < first_smallest:
            second_smallest = first_smallest
            first_smallest = n
        elif n < second_smallest and n != first_smallest:  # to handle duplicate cases
            second_smallest = n

    if second_smallest == float("inf"):
        print("There was no second smallest")
        return first_smallest, None
    else:
        return first_smallest, second_smallest


if __name__ == "__main__":
    nums = input_array("List of integer numbers")
    first, second = find_first_and_second_smallest(nums)
    print(first, second)

'''
------- Test cases ------- 

12 13 2 11 0 10
1 2 3 4 5 6 7       VVImp
7 7 7 7 7 7 7       Imp
3 2 2 1 1 2 3       v.v.v Imp   basically duplicate first and second smallest   
                    Need special condition otherwise both first and second will be same ie, 1, 1

'''
