from typing import List


# input an list of space-separated integers <array>
def input_array() -> list:
    return list(map(int, input().strip().split(" ")))


# If you don't want space at the end of it
def print_array(arr: List) -> None:
    list_of_string = list(map(str, arr))
    print(" ".join(list_of_string))


# If you want space at the end of it
def print_array_by_traversing(arr: List) -> None:
    for element in arr:
        print(element, end=" ")
    print()


if __name__ == "__main__":
    array = [1, 2, 3, 4]
    print_array(array)
    print_array_by_traversing(array)
