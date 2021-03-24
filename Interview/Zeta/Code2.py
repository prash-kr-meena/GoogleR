from Utils.Array import input_array

memo = {}


def helper(array_sum, n, x, arr, index, subset_sum) -> bool:
    if index >= n:
        if array_sum - subset_sum <= x:
            return True

        return False

    answer_when_choosing = False
    if arr[index] + subset_sum <= x:  # can  choose
        answer_when_choosing = helper(array_sum, n, x, arr, index + 1, subset_sum + arr[index])

    # not choosing
    answer_when_not_choosing = helper(array_sum, n, x, arr, index + 1, subset_sum)

    return answer_when_choosing or answer_when_not_choosing


def water_cooler(n, x, arr):
    array_sum = sum(arr)
    helper(array_sum, n, x, arr, 0, 0)

    pass


if __name__ == '__main__':
    n = int(input())
    x = int(input())
    array = input_array()
    water_cooler(n, x, array)

"""
Q1. There are n people and two identical water coolers to drink water ie w1 and w2. 
We have an array of size n such that each element stores time required by i-th person to drink water. 
At one time instant, only one person can be there on each water cooler.
Given a value x, defining the time till which the water coolers are operational, check whether all persons can drink water.

Input  : n = 3, x = 4
         A = [2, 4, 2]	

Output: YES
w1 = 2, 2
w2 = 4


A = [1 3 5 6]
X = 8
W1 = 6,1
W2 = 5,3 



W1     w2 

 1 3 5 6          x=8
Choose 1  [1]             -> 3 5 6          x=7
              Choose 3  [1 , 3]             - > 5 6          x=4
               Do not 3   []             - > 3 5 6          x=8


Do not 1   []             - > 3 5 6          x=8
            Do not 1   []             - > 3 5 6          x=8








20
20
w1 w2
10 10


4  = n 
8  = x
1 3 5 6  = arr


4  = n
8  = x
1 3 6 6  = arr
"""
