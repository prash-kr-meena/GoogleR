from Utils.Array import input_array


def frequency_sort(nums) -> list:
    freq = {}
    for num in nums:
        if freq.get(num) is not None:
            freq[num] += 1
        else:
            freq[num] = 1
    print(freq)

    pass


if __name__ == '__main__':
    array = input_array()
    sorted_array = frequency_sort(array)
    print(sorted_array)


"""
2 5 2 8 5 6 8 8
"""