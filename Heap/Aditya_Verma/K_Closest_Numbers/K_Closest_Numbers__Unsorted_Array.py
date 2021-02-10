from Utils.Array import input_array
from heapq import heapify, heappush, heappop


# Time  : O(n log k)
# Space : O(k)
def find_k_closest_numbers(arr, k, x):
    # heapify(array_of_tuple)
    # It works similar to the key= in sorted() function, as when we have a tuple it uses them element by element  Notice

    heap = []  # Max-Heap
    for num in arr:
        heappush(heap, (-abs(x - num), num))  # key->value mapping using tuple, Keys are negated to make a Max-Heap
        if len(heap) > k:
            heappop(heap)  # Ignored, as it will not contribute to our answer

    # [(-2, 7), (-1, 6), (-1, 4)]   : Heapified on key, so if the key is same, we get the  min later and max earlier

    print(heap)
    only_values = [pair[1] for pair in heap]
    return only_values


if __name__ == '__main__':
    array = input_array()
    k = int(input())
    x = int(input())
    print(find_k_closest_numbers(array, k, x))

"""
1 2 3 4 5
4 
3

1 2 3 4 5
4
-1
"""
