"""
Given an array of integers, find length of the largest subarray with sum equals to 0.

[1,4,5,2,-11,-1]        --> length 6

[1,5,10,12,1,0]         ---> [1,5,10,12,1,0,5]
[1,4,5,2,-11,-1]



[1, 2, 3, 10, -10 , 1]
[1, 3, 5, 15, 5 , 6]

[]

[15, -2, 2, -8, 1, 7, 10, 23]
[15, 13, 15, 7, 8, 15, 25, 48]


Approach s:
1. Brute force O(n2)
2. We can do this in O(1) using prefix sum
    The idea is to handle 0 separately and  as 0 will signify that the subaary from start index to that index is having 0 sum
    for others we can just have an hash-map and store all the prefix value in the map
    and when we see it again we know that there is a subaray from and index after it to the new found value

"""

if __name__ == '__main__':
    pass
