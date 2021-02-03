# Note : Same kind of implementation is present in the Aditya
from Recursion.Aditya_Verma.Hypothesis_Method.Tower_Of_Hanoi import toh


def tower_of_hanoi(disks, source, destination, helper) -> None:
    if disks == 0:
        return

    tower_of_hanoi(disks - 1, source, helper, destination)
    # Move the lowest disks from source to destination
    print("{} {}".format(source, destination))

    tower_of_hanoi(disks - 1, helper, destination, source)


if __name__ == '__main__':
    num_of_disks = int(input())
    tower_of_hanoi(num_of_disks, 'a', 'c', 'b')

    toh(num_of_disks, 'a', 'c', 'b')
