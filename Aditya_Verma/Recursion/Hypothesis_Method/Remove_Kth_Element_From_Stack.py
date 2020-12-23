from Abstract_Data_Types.StackADT import StackADT


# Here we treat k as 1 indexed
def remove_kth_element_from_top_of_stack(stack, kth):
    if stack is None or kth <= 0:
        raise ValueError("Invalid Parameters")

    if kth == 1:
        return stack.pop()

    top_element = stack.pop()
    removed_element = remove_kth_element_from_top_of_stack(stack, kth - 1)
    stack.push(top_element)
    return removed_element


if __name__ == "__main__":
    # s = StackADT([2, 4, 6, 0, 1])
    s = StackADT([9, 1, 2, 8, 4, 3])
    k = 2

    s.print()  # Not Removed
    popped_element = remove_kth_element_from_top_of_stack(s, k)
    print(popped_element, " < Removed")
    s.print()  # Kth element Removed
