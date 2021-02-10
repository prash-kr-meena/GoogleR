from heapq import heappush, heappop

from Utils.Array import input_array


def top_k_frequent_elements(arr, k) -> list:
    freq = {}  # map/dictionary
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # print(freq)

    heap = []  # creating a min heap
    for num_freq_mapping in freq.items():
        num, frequency = num_freq_mapping
        heappush(heap, (frequency, num))
        if len(heap) > k:
            heappop(heap)  # ignore the popped value

    # print(heap)
    return [pair[1] for pair in heap]


if __name__ == '__main__':
    array = input_array()
    k = int(input())
    result = top_k_frequent_elements(array, k)
    print(result)

"""
1 1 1 2 2 3
2


1
1
"""
