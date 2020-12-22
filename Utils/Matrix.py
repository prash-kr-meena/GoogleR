def get_filled_matrix(row_size, col_size, fill=0):
    return [[fill for _ in range(col_size)] for _ in range(row_size)]


def print_matrix(matrix):
    for row in matrix:
        print(row)


if __name__ == "__main__":
    print_matrix(get_filled_matrix(3, 10, 8))

    arr2D = [[16, 28, 60, 64],
             [22, 41, 63, 91],
             [27, 50, 87, 93],
             [36, 78, 87, 94]]

    print_matrix(arr2D)
