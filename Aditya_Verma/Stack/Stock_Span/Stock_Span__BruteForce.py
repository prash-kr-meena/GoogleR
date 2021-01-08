# O(n2) Time
# O(1) Space
def get_stock_span_values(nums) -> list:
    length = len(nums)
    stock_span_arr = [-1] * length

    for i in range(0, length):
        curr = nums[i]
        curr_span = 0
        for j in range(i, -1, -1):  # j is going backward from  i to 0
            if nums[j] <= curr:
                curr_span += 1
            else:
                break
        stock_span_arr[i] = curr_span

    return stock_span_arr


if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    result = get_stock_span_values(arr)
    print(result)

"""
10 5 11 10 20 12
100 80 60 70 60 75 85
"""
