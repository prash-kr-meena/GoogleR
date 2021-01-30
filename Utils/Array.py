from typing import List


# input an list of space-separated integers <array>
def input_array(prompt) -> list:
    print(prompt + " : ")
    return list(map(int, input().strip().split()))


# If you don't want space at the end of it
def print_array_inline(arr: List) -> None:
    list_of_string = list(map(str, arr))
    print(" ".join(list_of_string))


# If you want space at the end of it
def print_array_by_traversing(arr: List) -> None:
    for element in arr:
        print(element, end=" ")
    print()


def print_array_multiline(arr: List) -> None:
    for element in arr:
        print(element)


if __name__ == "__main__":
    array = [1, 2, 3, 4]
    print_array_inline(array)
    print_array_by_traversing(array)
