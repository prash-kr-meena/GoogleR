# Time : O(n^2)
# Space : O(n) recursion space + O(n) extra space insertion code
# Yes insertion code can be done in constant space as well (Here making an extra array )

def insert_num_iteratively(sorted_array, k) -> list:
    final_sorted_list = []
    number_has_been_inserted = False

    for num in sorted_array:
        if not number_has_been_inserted and num > k:
            final_sorted_list.append(k)  # Number to be inserted
            final_sorted_list.append(num)  # The original number in the order
            number_has_been_inserted = True
        else:
            final_sorted_list.append(num)

    if not number_has_been_inserted:  # case when the number has to be inserted at the end
        final_sorted_list.append(k)

    return final_sorted_list


def sort_array(A) -> list:
    # Edge case
    if A is None or len(A) == 0:
        print("Invalid Input")

    # Base Case - Single Element Array Is Inherently Sorted
    if len(A) == 1:
        return A

    last_num = A.pop()  # Decreasing the input
    sorted_array = sort_array(A)  # Here it is of one less size, then our original problem

    # Induction step : need to insert the last_num in the sorted_array, to fully sort current array A - Insertion Sort
    full_size_sorted_array = insert_num_iteratively(sorted_array, last_num)
    return full_size_sorted_array


if __name__ == "__main__":
    # arr = [5, 6, 3, 4, 2, 1, 0]
    # arr = [1, 2, 3, 4, 5]
    arr = [5, 4, 2, 0, -1]
    print(sort_array(arr))
