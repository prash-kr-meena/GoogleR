def min_max_in_n_comparisons(A):
    minimum = float('inf')
    maximum = float('-inf')
    for a in A:
        if a > maximum:
            maximum = a
        if a < minimum:
            minimum = a
    return minimum, maximum


arr = [1, 3, 4, 2, 0, 7, 1, 3]
print(min_max_in_n_comparisons(arr))

'''
[1000, 11, 445, 1, 330, 3000]
[1, 3, 4, 2, 0, 7, 1, 3]
'''
