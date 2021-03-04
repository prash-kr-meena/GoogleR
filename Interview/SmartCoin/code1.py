from Utils.Array import input_array

"""
This question is the exact question, that we have solve in the sde sheet
with the name, Find_Duplicate_In_Array.py 
"""


def find_duplicate(arr) -> int:
    n = len(arr)
    slow = fast = arr[0]

    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break

    # slow and fast are at position
    # finding the intersection point
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]

    # at intersection
    return slow  # or fast


if __name__ == '__main__':
    array = input_array()
    print(find_duplicate(array))

"""
1 2 3 2
1 1 1 1
1 2 2 1
"""
