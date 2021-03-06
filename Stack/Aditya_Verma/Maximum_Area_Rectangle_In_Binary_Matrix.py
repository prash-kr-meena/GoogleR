from Stack.Aditya_Verma.Maximum_Area_Histogram import mah
from Utils.Matrix import input_matrix

"""
Time  : O(n * m)
Space : O(n * m)
"""


def create_building_for_this_level(rolling_buildings, buildings):
    # Notice : modifying rolling_buildings
    for index, building_height in enumerate(buildings):
        if building_height == 0:  # Will not include buildings, jo hava me hai
            rolling_buildings[index] = 0
        else:
            rolling_buildings[index] = rolling_buildings[index] + building_height


def find_max_area_rectangle_in_binary_matrix(matrix):
    if len(matrix) == 0:  # Edge Case
        return 0

    columns = len(matrix[0])  # considering column size would be fixed, Ie No Jagged Array
    rolling_buildings = [0] * columns  # Notice : this is a rolling array

    max_area = float("-inf")
    for buildings in matrix:
        create_building_for_this_level(rolling_buildings, buildings)  # updating rolling_buildings
        max_area_for_these_building = mah(rolling_buildings)  # Notice : using maximum_area_histogram
        max_area = max(max_area_for_these_building, max_area)

    return max_area


if __name__ == '__main__':
    arr2D = input_matrix()
    max_area = find_max_area_rectangle_in_binary_matrix(arr2D)
    print(max_area)

"""
row : 4
col : 4
0 1 1 0
1 1 1 1
1 1 1 1
1 1 0 0


row : 3
col : 3
0 1 1
1 1 1
0 1 1


row : 4
col : 5
1 0 1 0 0 
1 0 1 1 1 
1 1 1 1 1 
1 0 0 1 0

"""
