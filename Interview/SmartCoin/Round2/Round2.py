"""
 n ---> [ 1 2 3 ... n ]

 eg. 1 2 3
     2 3 1
     3 1 2
     .
     .
     .
     [3] [2] [1]  ==> 3! possibilities
"""
chosen = set()


def print_permutations(arr, output="", idx=0, ) -> None:
    n = len(arr)

    if idx >= n:
        print(output)
        return

    for e in arr:
        if e in chosen:
            continue
        chosen.add(e)
        print_permutations(arr, output + str(e), idx + 1)
        chosen.remove(e)


if __name__ == '__main__':
    num = int(input())
    array = [i for i in range(1, num + 1)]
    print_permutations(array)
