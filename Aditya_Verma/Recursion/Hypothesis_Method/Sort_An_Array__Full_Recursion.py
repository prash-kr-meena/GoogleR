# Time : O(n^2)
# Space : O(n) for recursion of sort_array function, + O(n) for recursion of insert method


# Even thought its inplace, but the recursion takes O(n) space
def insert_num_recursively(sorted_array, k) -> None:
    if sorted_array is None:
        raise ValueError("Invalid Input")

    n = len(sorted_array)
    if n == 0 or sorted_array[n - 1] < k:
        sorted_array.append(k)
        return

    last_num = sorted_array.pop()  # getting it from the end
    insert_num_recursively(sorted_array, k)  # sorted_array, has decreased size
    sorted_array.append(last_num)  # adding it back to the end


def sort_array(A) -> None:
    # Edge case
    if A is None or len(A) == 0:
        print("Invalid Input")

    # Base case - Single element array is inherently sorted
    if len(A) == 1:
        return

    last_num = A.pop()  # decreasing the input
    sort_array(A)  # here it is of one less size, then our original problem

    # induction step : need to insert the last_num in the sorted_array, to fully sort current array A
    insert_num_recursively(A, last_num)  # inplace


if __name__ == "__main__":
    # arr = [5, 6, 3, 4, 2, 1, 0]
    # arr = [1, 2, 3, 4, 5]
    arr = [5, 4, 2, 0, -1]
    sort_array(arr)
    print(arr)
