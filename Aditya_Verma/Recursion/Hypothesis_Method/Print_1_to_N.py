def print_to_n(n):
    if n == 1:  # base condition
        print(1)
        return

    print_to_n(n - 1)  # induction
    print(n)  # hypothesis


if __name__ == "__main__":
    print_to_n(7)
