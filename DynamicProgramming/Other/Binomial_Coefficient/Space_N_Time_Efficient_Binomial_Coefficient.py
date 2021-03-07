"""
GfG : https://www.geeksforgeeks.org/space-and-time-efficient-binomial-coefficient/
"""


# Python program to calculate nCr C(n, r)

# Returns value of Binomial Coefficient C(n, k)
def space_n_time_efficient_binomial_coefficient(n, r):
    if r > n or r < 0:
        return Exception("Invalid r value")

    if r > n - r:  # since C(n, r) = C(n, n - r)
        r = n - r

    res = 1  # initialize result

    # Calculate value of [n * (n-1) *---* (n-k + 1)] /  [k * (k-1) *----* 1]
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return res


if __name__ == '__main__':
    n_of_nCr = int(input())
    r_of_nCr = int(input())
    print(space_n_time_efficient_binomial_coefficient(n_of_nCr, r_of_nCr))

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
