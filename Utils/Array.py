from typing import List


# input an list of space-separated integers <array>
def input_array(prompt="arr : ") -> list:
    return list(map(int, input(prompt).strip().split()))


# If you don't want space at the end of it
def print_array_inline(arr: list) -> None:
    list_of_string = list(map(str, arr))
    print(" ".join(list_of_string))


# If you want space at the end of it
def print_array_by_traversing(arr: list) -> None:
    for element in arr:
        print(element, end=" ")
    print()


def print_array_multiline(arr: list) -> None:
    for element in arr:
        print(element)


def reverse_array_inplace(arr: list, i: int, j: int):
    # Reverse Array Inplace b/w i to j, Both Inclusive
    n = len(arr)

    if i < 0 or i > n - 1 or j < 0 or j > n - 1:
        return Exception("Out of index")

    if j < i:
        return Exception("j > i Not allowed")

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1


if __name__ == "__main__":
    array = [1, 2, 3, 4]
    print_array_inline(array)
    print_array_by_traversing(array)
    reverse_array_inplace(array, 0, len(array) - 1)
    print("After reverse : ", array)
