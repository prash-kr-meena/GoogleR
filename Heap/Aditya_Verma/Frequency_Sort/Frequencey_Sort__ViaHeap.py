from Utils.Array import input_array
from Utils.Map import get_frequencies_in_integer_array

from heapq import heapify, heappop, heappush

"""
UE = unique_elements

Space  : O(UE)  for map  + O(UE) for heap
Time   : O(UE    log UE)  * freq
            O(n) in building the map of freq
            O(UE log UE) for sorting, the heap as we are pulling out all UE elements from it
            and then inside another for loop, we are going till the freq
            
        Effectively its a bit smaller then O(n log n)
        
        for eg. let there be an input, which is given 9000 times
        [4, 4, 4, 4, 4, 4, 4, ...... 9k times]
        
        now when you create a Map, in O(n) time, that mapi will have only one entry  {4:9000}
        now you are doing    O(UE    log UE)  * freq    operations
        ie O(1 log 1) * 9K  => 9k        
        which is basically O(n) operations
        
        While in the comparison method, you would be comparing each and every element
        ie O(9k  log 9k) operation
"""


# Out of Place algorithm
def frequency_sort(nums):
    freq = get_frequencies_in_integer_array(nums)

    # Instead of writing a comparison function, we will gonna use Heap, and heapify on the basis of freq
    # create an empty heap, (which underline is a list)
    heap = []  # We want to use it as a MaxHeap, so need to negate the value of freq, so that freq comes on top
    for number, frequency in freq.items():
        heappush(heap, (-frequency, number))  # we put frequency first, as we are heapify-ing on the basis of freq
    # print(heap)

    freq_sorted_array = []
    while len(heap) != 0:
        frequency, number = heappop(heap)
        frequency *= -1  # Making Freq +ve Again
        for i in range(frequency):
            freq_sorted_array.append(number)

    return freq_sorted_array


if __name__ == '__main__':
    array = input_array()
    f_sorted_array = frequency_sort(array)
    print(f_sorted_array)

"""
2 5 2 8 5 6 8 8 
"""
