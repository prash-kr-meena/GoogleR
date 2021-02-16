from Utils.Array import input_array
from Utils.Map import get_frequencies_in_integer_array

"""
Space  : O(unique_elements) for map
Time   : O(n log n)
            O(n) in building the map of freq
            O(n log n) for sorting
"""


def frequency_sort(nums):
    freq = get_frequencies_in_integer_array(nums)

    # While sorting we want to give first priority to Frequency Then to value of item
    nums.sort(key=lambda number: (-freq[number], number))  # Lambda is basically the compare function : Notice
    # Here, for number we want natural ordering
    # But, for the (freq of that number) freq[number], we want a reverse order, so we put -ve


if __name__ == '__main__':
    array = input_array()
    frequency_sort(array)
    print(array)

"""
2 5 2 8 5 6 8 8 
"""
