"""
GfG Article : https://www.geeksforgeeks.org/binomial-coefficient-dp-9/
Google Docs : https://docs.google.com/document/d/11EzTzksWc929SXEBTMwAYCMigWVNKn8NQfigWpyK1JQ/edit#

Write a function that takes two parameters n and k and returns the value of Binomial Coefficient C(n, r).
eg.
    Input: n = 4 and r = 2
    Output: 6
    Explanation: 4 C 2 is 4!/(2!*2!) = 6

    Input: n = 5 and r = 2
    Output: 10
    Explanation: 5 C 2 is 5!/(3!*2!) = 20
"""

"""
To solve this we need to know 

The recurrence formula for nCr 
    nCr = (n-1)C(r-1) + (n-1)Cr
    and
    nCn = nC0 = 1       ie, when r == n , or r == 0     then nCr = 1


nCr =  _____n!_____  
         r! (n-r)!

Also r can't be greater then n
ie,       0 <= r <= n       Otherwise, any other value of r, should be handled by the edge case
"""

"""
This has overlapping sub-problems, and hence we should use dynamic programming to solve this
memoization or bottom-up tabular
"""


# Remember, recursion is not free it takes space

# Time : exponential 2^n
# Space : at max O(n) node will be waiting at any particular time, in the function stack-frame to be completed
def binomial_coefficient(n, r):
    if r < 0 or r > n:
        return Exception("Not valid r value")  # or return 0

    if r == n or r == 0:  # Base Case
        return 1

    return binomial_coefficient(n - 1, r - 1) + binomial_coefficient(n - 1, r)


if __name__ == '__main__':
    n_of_nCr = int(input())
    r_of_nCr = int(input())
    print(binomial_coefficient(n_of_nCr, r_of_nCr))

"""
4 = n
2 = r
Output = 6 
"""

"""
5  = n
2  = r
Output = 10
"""

"""
5  = n
6  = r      << Invalid R
Output = 10
"""
