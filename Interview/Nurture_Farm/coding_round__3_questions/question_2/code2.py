from Utils.Matrix import get_filled_matrix, print_matrix

"""
The question was on graphs,
where the question looked difficult but it was actually very easy, and didn't had any concept
related to graph, even graph traversal

it was all basic loops, and
You were given a graph, you needed to fuigre out the triods (3 nodes in cycle - could be 0 to many)
and then you need to find connection of the nodes outside of the triod (ie, basically degree of the nodes) but
you don't count the nodes that are present in the triod,
you need to sum these degree of all the three nodes in that triod
and you need to do this for all the triods

and then return the minimum of all of them,
In case there was no triod found you can return -1

"""


def find_friends_outside_trio(subject, matrix, targe1, target2):
    count = 0

    for target in range(len(matrix)):
        if target == targe1 or target == target2:
            continue
        if matrix[subject][target]:
            count += 1

    print(f"outside friend of {subject} with {targe1}, {target2} is ", count)
    return count


def bestTrio(friends_nodes, friends_from, friends_to):
    minimum_friend_score = float("+inf")
    edges = len(friends_from)  # len(friends_to)

    n = friends_nodes
    matrix = get_filled_matrix(n + 1, n + 1, None)  # extra one size
    for i, j in zip(friends_from, friends_to):
        matrix[i][j] = True

    # going row wise
    for main_person in range(1, n):
        persons_friend = matrix[main_person]
        for person_1 in range(1, n):  # as we start from 1, and not 0
            for person_2 in range(person_1 + 1, n):
                if persons_friend[person_1] is True and persons_friend[person_2] is True:
                    # found a trio
                    print(main_person, person_1, person_2)
                    total_outside_friends = 0
                    total_outside_friends += find_friends_outside_trio(main_person, matrix, person_1, person_2)
                    total_outside_friends += find_friends_outside_trio(person_1, matrix, person_2, main_person)
                    total_outside_friends += find_friends_outside_trio(person_2, matrix, person_1, main_person)

                    minimum_friend_score = min(total_outside_friends, minimum_friend_score)
            pass
        pass

    print_matrix(matrix)
    print(minimum_friend_score)
    return minimum_friend_score


# Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    friends_nodes, friends_edges = map(int, input().rstrip().split())

    friends_from = [0] * friends_edges
    friends_to = [0] * friends_edges

    for i in range(friends_edges):
        friends_from[i], friends_to[i] = map(int, input().rstrip().split())

    result = bestTrio(friends_nodes, friends_from, friends_to)

    # fptr.write(str(result) + '\n')
    # fptr.close()
"""
5 6
1 2
1 3
2 3
2 4
3 4
4 5
"""
