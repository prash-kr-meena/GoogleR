from Aditya_Verma.Stack.Index__Greater_n_Smaller_Nums_To_Left_n_Right.NSL_Index import \
    indexes_of_next_smaller_element_to_left
from Aditya_Verma.Stack.Index__Greater_n_Smaller_Nums_To_Left_n_Right.NSR_Index import \
    indexes_of_next_smaller_element_to_right

""" MAH   |   Maximum Area Of Histogram """


def sanitize_input_for_better_calculations(nums):
    # For making calculations correct for case of NSR
    # Adding a value at end, so instead of putting -1 for the original last element,
    # we can put, our new fake last element's index

    nums.append(0)  # A building with 0 height
    # no need to put on left side, as its before 0'th index, so it will get -1 as index only
    # Notice : modifying the original array here


def mah(buildings) -> int:  # Return Max Area
    sanitize_input_for_better_calculations(buildings)  # modifying the actual array
    # print("sanitized : ", buildings)

    nsr_index = indexes_of_next_smaller_element_to_right(buildings)
    nsl_index = indexes_of_next_smaller_element_to_left(buildings)
    # print("nsr_index : ", nsr_index)
    # print("nsl_index : ", nsl_index)

    building_span = [right_index - left_index for right_index, left_index in zip(nsr_index, nsl_index)]  # Notice
    building_span = [span - 1 for span in building_span]  # Subtracting 1, as we are counting the curr building twice
    # print("building_span : ", building_span)

    # Now we have both, the building_span and the original heights of building -> We can find the area
    histogram_areas = [building_height * span for building_height, span in zip(buildings, building_span)]
    # print("histogram_areas : ", histogram_areas)

    return max(histogram_areas)


if __name__ == '__main__':
    buildings = list(map(int, input().strip().split()))
    print(mah(buildings))

"""
6 2 5 4 5 1 6
"""
