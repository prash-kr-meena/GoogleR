from typing import List

from Utils.Array import input_array

"""
This is the question that he asked
https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/

The current solution is not complete
put_it_at_correct_location   method needs to be completed
which will be a recursive method
"""

IGNORE_CONSTANT = -1
PUSH_CONSTANT = -2


def count_positive_values(A: List[int]) -> int:
    count = 0
    for element in A:
        if element > 0:
            count += 1
    return count


def mark_all_negative_and_greater_number_as_un_useful(A: List[int], max_number: int) -> None:
    for i in range(len(A)):
        if A[i] <= 0 or A[i] > max_number:
            A[i] = IGNORE_CONSTANT


def put_it_at_correct_location(A, index):
    # base cases
    value = A[index]
    if value == IGNORE_CONSTANT:
        return

    index = index + 1
    if index == value:
        return

    next_index = value
    A[index] = PUSH_CONSTANT

    pass


def find_first_minimum_positive_not_present_in_the_array(A):
    positive_count = count_positive_values(A)

    range_min = 1
    range_max = positive_count + 1

    mark_all_negative_and_greater_number_as_un_useful(A, positive_count)

    for i in range(len(A)):
        put_it_at_correct_location(A, i)

    print(A)

    pass


if __name__ == '__main__':
    array = input_array()
    find_first_minimum_positive_not_present_in_the_array(array)

"""
Input:  2  3  7  6  8  -1  -10  15
Output: 1

Input:  2  3  -7  6  8  1  -10  15
Output: 4

Input: 1  1  0  -1  -2
Output: 2



[2, 3, IGNORE, 6, IGNORE, 1, IGNORE, IGNORE]

"""

"""
Input:  {2, 3, 7, 6, 8, -1, -10, 15}
Output: 1

Input:  { 2, 3, -7, 6, 8, 1, -10, 15 }
Output: 4

Input: {1, 1, 0, -1, -2}
Output: 2


{ 2, 3, -7, 6, 8, 1, -10, 15 }
Range : 1 to 6+1   1-7  ignored all the -ve numbers , count all +ves

Ignore : INT_MIN

Ignore all -ve and number more then 6

{ 2, 3, INT_MIN, 6, INT_MIN, 1, INT_MIN, INT_MIN }
{ 2, 3, INT_MIN, 6, INT_MIN, 1, INT_MIN, INT_MIN } 
 temp = 3 != INT_MIN

  1 
{INT_MAX  2, 3 , INT_MAX , INT_MAX ,   , 6 }    temp = 1
{1  2, 3 , INT_MAX , INT_MAX ,   , 6 }    temp = 1


{ 1 , 2, 3, INT_MIN, 6, INT_MIN, INT_MIN } 







Time : O(n) * max_num
Space : O(1)
---------------------------
Map or Set
Space : O(N)  
I could neglect the -ve number
{-1 -2 , 1,2,3,4,5,6,7,8,9}
{2}

Formula to find sum of first n natural number
{ 2, 3, -7, 6, 8, 1, -10, 15 }
{ -10, -7 , 2, 3, 6, 8, 1, 15 } []

6+ve & 2-ve
Range decreased -> 1 to  N+1 -2
{ 2, 3, 6, 8, 1, 15 } []         remove 0 as well, consider all +ve number only

{ 2, 3, 6, Int_MIN, 1, INT_MIN } []
{ 2, 3, 6, 1,} []
  


4

Maximum possible answer for any given array of size n
In what range the answer will be, for any given array of size n

{1,2,3,4,5,6,7,8,9}
10
N 
[1-N+1]



[-1 -2 -3 -4  .. …  -200000000]
TIme : O(n)
---------------------------
Sorting
TIme : (n log n)
Space : (1)

---------------------------
Required
Time O(n)
Space O(1)



{}
1

[0]
1

[-1]
1

[100]
1

[1 2 3 4]
5

"""
