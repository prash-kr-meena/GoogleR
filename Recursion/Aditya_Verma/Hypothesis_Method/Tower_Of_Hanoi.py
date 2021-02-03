def toh(disks, source, destination, helper) -> int:
    # Number of steps it will take to transfer the disks from one tower to another

    # Base Case
    if disks == 1:
        print("move disk {} from {} -> {}".format(disks, source, destination))
        return 1  # only one step needed

    # Hypothesis
    steps_to_move_remaining_disks__from_src_helper = toh(disks - 1, source, helper, destination)

    # Induction step
    print("move last disk({}) from {} -> {}".format(disks, source, destination))
    steps_to_move_last_disk__from_src_dest = 1

    steps_to_move_remaining_disks__from_helper_dest = toh(disks - 1, helper, destination, source)

    return steps_to_move_remaining_disks__from_src_helper + steps_to_move_last_disk__from_src_dest + steps_to_move_remaining_disks__from_helper_dest


if __name__ == "__main__":
    disks = 3
    print(toh(disks, 'SOURCE', 'DESTINATION', 'HELPER'))
