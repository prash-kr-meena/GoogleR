from Utils.Array import input_array

"""
 Find the largest and second largest elements in an array

 Important part could be handling the corner cases, like handling the duplicates (even if you sort it)

 Approach 1 : sorting   O(n lg n)
 Approach 2 : 1 Pass    O(n)
"""


def find_first_and_second_largest__not_handling_duplicity(nums) -> (int, int):
    first_largest = second_largest = float("-inf")

    for n in nums:
        if n > first_largest:
            second_largest = first_largest
            first_largest = n
        elif n > second_largest:  # Not handling duplicate cases Notice
            second_largest = n

    if second_largest == float("-inf"):
        print("There was no second smallest")
        return first_largest, None
    else:
        return first_largest, second_largest


if __name__ == "__main__":
    array = input_array("List of integer numbers : ")
    first, second = find_first_and_second_largest__not_handling_duplicity(array)
    print(first, second)

"""
------- Test cases ------- 

12 13 2 11 0 10
1 2 3 4 5 6 7       VVImp
7 7 7 7 7 7 7       Imp
3 2 2 1 1 2 3       v.v.v Imp   basically duplicate first and second smallest   
                    Need special condition otherwise both first and second will be same ie, 1, 1

"""
