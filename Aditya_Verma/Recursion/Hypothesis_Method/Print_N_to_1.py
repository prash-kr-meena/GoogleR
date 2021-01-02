# Forward Implementation
def print_to_n_reverse(n):
    if n == 1:  # Base Condition
        print(1, end=" ")
        return

    print(n, end=" ")  # Induction
    print_to_n_reverse(n - 1)  # Hypothesis


# Backward implementation
# - Here backward implementation, would be a bit typical to do,
# - Forward implementation makes more sense, if you think in terms of the input n

if __name__ == "__main__":
    print_to_n_reverse(7)
