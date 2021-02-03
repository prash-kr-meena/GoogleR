# Backward implementation
from sys import setrecursionlimit


def print_to_n(n):
    if n == 1:  # Base condition
        print(1, end=" ")
        return

    print_to_n(n - 1)  # Hypothesis
    print(n, end=" ")  # Induction


# Forward implementation
# - It will become a bit complex, as we would require an extra index field to go forward in the sequence
# - Which is not ideal here as you don't have a sequence

if __name__ == "__main__":
    setrecursionlimit(11000)
    print_to_n(7)
