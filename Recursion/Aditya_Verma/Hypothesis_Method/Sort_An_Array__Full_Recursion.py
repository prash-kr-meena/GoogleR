# Time : O(n^2)
# Space : O(n) for recursion of sort_array function, + O(n) for recursion of insert method


# Even thought its inplace, but the recursion takes O(n) space
def insert_num_recursively(sorted_array, k) -> None:
    # Edge Case
    if sorted_array is None:
        raise ValueError("Invalid Input")

    n = len(sorted_array)
    if n == 0 or sorted_array[n - 1] < k:  # If array is empty   OR   Last element of the array is smaller then K
        sorted_array.append(k)
        return

    last_num = sorted_array.pop()  # Getting it from the end
    insert_num_recursively(sorted_array, k)  # sorted_array, has decreased size by 1    ---  Hypothesis Method
    sorted_array.append(last_num)  # Adding it back to the end                          --- Part of Hypothesis

    # No Induction Step : Any step to get the answer


def sort_array(A) -> None:
    # Edge case
    if A is None or len(A) == 0:
        print("Invalid Input")

    # Base case - Single element array is inherently sorted
    if len(A) == 1:
        return

    last_num = A.pop()  # Decreasing the input
    sort_array(A)  # Here it is of one less size, then our original problem

    # Induction Step : need to insert the last_num in the sorted_array, to fully sort current array A
    insert_num_recursively(A, last_num)  # Inplace


if __name__ == "__main__":
    # arr = [5, 6, 3, 4, 2, 1, 0]
    # arr = [1, 2, 3, 4, 5]
    arr = [5, 4, 2, 0, -1]
    sort_array(arr)
    print(arr)
