from Utils.Array import input_array

"""
Given a list of x,y
can you tell if all these points lie on the same line
"""


def verify_straight_line(xy) -> bool:
    slopes = set()
    first_point_slope = xy[0][1] / xy[0][0]
    slopes.add(first_point_slope)
    for i in range(1, len(xy)):
        point = xy[i]
        slope = point[1] / point[0]
        if slope not in slopes:
            return False
    return True


if __name__ == '__main__':
    x_s = input_array()
    y_s = input_array()
    xy = [xy for xy in zip(x_s, y_s)]

    print(verify_straight_line(xy))
"""
1 2 3
1 2 3
"""
