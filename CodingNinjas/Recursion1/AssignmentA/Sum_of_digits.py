def sum_digits(num):
    # Base case
    if num == 0:
        return 0

    # Hypothesis
    remaining_num, last_digit = divmod(num, 10)
    sum_of_remaining_digits = sum_digits(remaining_num)

    # Induction
    return sum_of_remaining_digits + last_digit


if __name__ == '__main__':
    number = int(input())
    print(sum_digits(number))
