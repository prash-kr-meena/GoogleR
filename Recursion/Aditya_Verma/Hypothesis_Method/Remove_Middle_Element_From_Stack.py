from Abstract_Data_Type.StackADT import StackADT
from Recursion.Aditya_Verma.Hypothesis_Method.Remove_Kth_Element_From_Stack import remove_kth_element_from_top_of_stack


def remove_middle_element_of_stack(stack) -> None:
    middle = (stack.size() // 2) + 1

    s.print()  # Not Removed
    removed_element = remove_kth_element_from_top_of_stack(stack, middle)
    print(removed_element, " < Removed")  # You can return removed element if you want Notice
    s.print()  # Kth element Removed


if __name__ == "__main__":
    # s = StackADT([2, 4, 6, 0, 1])  # Odd
    s = StackADT([9, 1, 2, 8, 4, 3])  # Even
    remove_middle_element_of_stack(s)
