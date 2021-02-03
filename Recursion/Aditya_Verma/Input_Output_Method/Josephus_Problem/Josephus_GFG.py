# index = From where we start counting
def find_josephus(persons, k, sword_index=0) -> int:
    # Base Case
    if len(persons) == 1:
        return persons[0]

    size = len(persons)

    # Hypothesis
    # first person that has to be deleted
    delete_index = (sword_index + k) % size
    del persons[delete_index]

    # The next index to count from is in actuality delete_index+1 -> and as it can go out of bound we need to use mod
    # ie, (delete_index+1) % size

    # But as we have removed the element, so the current element that comes on this index will be our start NOTE
    return find_josephus(persons, k, delete_index % size)

    # No induction step is required here,
    # as we are not using the returned value, because it is of no use to us


def find_last_living_person(N, K):
    persons = []
    for _ in range(1, N + 1):
        persons.append(_)
    # print(persons)

    return find_josephus(persons, K - 1)


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().strip().split()))
        print(find_last_living_person(N, K))
