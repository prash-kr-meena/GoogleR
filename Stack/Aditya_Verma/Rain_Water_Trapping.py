from Utils.Array import input_array


def find_maximum_left_for_each(arr, n) -> list:
    # Going from left to right
    maxL = [None] * n
    maximum = float("-inf")

    for idx, val in enumerate(arr):
        maximum = max(maximum, val)
        maxL[idx] = maximum  # Updating the maxL array, for every element of arr

    return maxL


def find_maximum_right_for_each(arr, n) -> list:
    # Going from right to left
    maxR = [None] * n
    maximum = float("-inf")

    for idx in range(n - 1, -1, -1):  # start = n-1, stop = -1, step = -1
        val = arr[idx]
        maximum = max(maximum, val)
        maxR[idx] = maximum  # Updating the maxR array, for every element of arr

    return maxR


def find_water(arr) -> int:
    n = len(arr)
    maxL = find_maximum_left_for_each(arr, n)
    maxR = find_maximum_right_for_each(arr, n)

    water_at_each_building = [min(left_tall_building, right_tall_building) - curr_building_height
                              for left_tall_building, right_tall_building, curr_building_height in zip(maxL, maxR, arr)]

    total_water = sum(water_at_each_building)
    return total_water

    # print(maxL)
    # print(maxR)
    # print(water_at_each_building)


if __name__ == '__main__':
    building_heights = input_array()  # A non-negative array, as these are buildings height
    water = find_water(building_heights)
    print(water)

"""
3 0 0 2 0 4  => 10
0 1 0 2 1 0 1 3 2 1 2 1  =>  6
2 0 2  =>  2
3 0 2 0 4  =>  7
"""
