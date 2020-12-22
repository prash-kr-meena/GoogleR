def print_to_n_reverse(n):
    if n == 1:  # base condition
        print(1)
        return

    print(n)  # induction
    print_to_n_reverse(n - 1)  # hypothesis


if __name__ == "__main__":
    print_to_n_reverse(7)
