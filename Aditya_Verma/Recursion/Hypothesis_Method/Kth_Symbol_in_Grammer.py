# LeetCode - Submitted successfully
# https://leetcode.com/problems/k-th-symbol-in-grammar/

def find_symbol_in_grammer__even_odd_approach(n: int, k: int) -> str:
    # Base Case
    if n == 1 and k == 1:
        return '0'

    # Hypothesis
    parent_symbol = find_symbol_in_grammer__even_odd_approach(n - 1, (k + 1) // 2)
    # parent_symbol  -> 0 or 1

    # Induction Step
    k_is_odd = k % 2 == 1

    if k_is_odd:
        return parent_symbol  # same as parent
    else:
        return '1' if parent_symbol == '0' else '0'
        # opposite of parent symbol


def find_symbol_in_grammer__symmetry_approach(n, k) -> int:
    """
    This is the approach discussed in the video, Aditya Verma
    """

    if n == 1 and k == 1:
        return 0

    mid = (2 ** (n - 1)) // 2

    if k <= mid:
        return find_symbol_in_grammer__symmetry_approach(n - 1, k)
    else:
        tmp = find_symbol_in_grammer__symmetry_approach(n - 1, k - mid)
        return 1 if tmp == 0 else 0


if __name__ == "__main__":
    # n, k = 1, 1
    # n, k = 2, 1
    # n, k = 2, 2
    n, k = 4, 5
    print(find_symbol_in_grammer__even_odd_approach(n, k))
    print(find_symbol_in_grammer__symmetry_approach(n, k))
