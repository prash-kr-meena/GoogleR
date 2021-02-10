from heapq import heapify, heappush, heappop
from typing import List

from Utils.Array import input_array

"""
https://leetcode.com/problems/find-k-closest-elements/

This problem can also be solved by binary search, which
    https://leetcode.com/problems/find-k-closest-elements/discuss/915047/Finally-I-understand-it-and-so-can-you.
    https://leetcode.com/problems/find-k-closest-elements/discuss/1011114/Python-Binary-search%2BTwo-pointer-w-comments
    https://leetcode.com/problems/find-k-closest-elements/discuss/909705/Cleaner-Heap-approach-andand-Binary-search-approach-solution
"""


# Total Time : O(n + k log n)
def find_k_closest_elements(arr: List[int], k: int, x: int) -> List[int]:
    heap = [(abs(x - num), num) for num in arr]  # Min-Heap, pair(+ve key, +ve value), heapify by key then by value
    heapify(heap)  # O(n) Time      Top will be min,

    res = []
    for i in range(k):  # O(k lg n)
        value = heappop(heap)[1]
        res.append(value)

    res.sort()
    return res


if __name__ == '__main__':
    array = input_array()
    k = int(input())
    x = int(input())
    print(find_k_closest_elements(array, k, x))

"""
1 2 3 4 5
4 
3

1 2 3 4 5
4
-1
"""
