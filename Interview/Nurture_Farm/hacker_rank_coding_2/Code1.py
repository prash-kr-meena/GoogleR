# Looks like bfs travesal of the map

# Note : Bad code, could have implemented better way, Few test cases still failed, like 5 out of 15

import math
import os
import random
import re
import sys

#
# Complete the 'order' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. UNWEIGHTED_INTEGER_GRAPH city
#  2. INTEGER company
#

#
# For the unweighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i].
#
#
from collections import deque

NOT_CONNECTED = 0
CONNECTED = 1
VISITED = True
UN_VISITED = False


def get_filled_matrix(row_size, col_size, fill=0):
    return [[fill for _ in range(col_size)] for _ in range(row_size)]


def bfs_elements(adj_matrix, vertex, visited) -> list:
    result = []

    n = len(adj_matrix)
    level = 0
    counter = 1

    queue = deque()
    queue.append((vertex, 0))
    visited[vertex] = VISITED  # marking visited

    while len(queue) != 0:
        q_size = len(queue)

        while q_size != 0:

            vertex_i, level = queue.popleft()

            if vertex_i != vertex:
                result.append((vertex_i, level + counter))
                # print(vertex_i, end=" ")  # process

            for vertex_j in range(n):
                if adj_matrix[vertex_i][vertex_j] == CONNECTED and visited[vertex_j] == UN_VISITED:
                    # two vertices are adjacent, and not visited, so put all into queue to process later
                    queue.append((vertex_j, level + counter))
                    visited[vertex_j] = VISITED

                    # to handle case, when the vertex is in queue, and you did not mark it visited and another vertex
                    # that you took out was connected to the one present in the queue, so it got pushed multiple times
                    # so when you push it to the queue mark it as visited, so no duplicates will appear in the queue

            q_size -= 1
        counter += 1

    return result


def get_element_bfs_order(adj_matrix, vertex_to_start_from) -> list:
    n = len(adj_matrix)

    visited = [UN_VISITED] * n  # boolean array
    return bfs_elements(adj_matrix, vertex_to_start_from, visited)


def order(city_nodes, city_from, city_to, company):
    vertices = city_nodes  # No of Vertices,
    edges = len(city_from)  # No of Edges

    adj_matrix = get_filled_matrix(vertices + 1, vertices + 1, NOT_CONNECTED)
    for i in range(edges):
        adj_matrix[city_from[i]][city_to[i]] = CONNECTED
        adj_matrix[city_to[i]][city_from[i]] = CONNECTED

    bfs_order = get_element_bfs_order(adj_matrix, company)
    sorted_bfs = sorted(bfs_order, key=lambda pair: (pair[1], pair[0]))
    # print(sorted_bfs)
    final_res = [pair[0] for pair in sorted_bfs]
    print(final_res)
    return final_res


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    city_nodes, city_edges = map(int, input().rstrip().split())

    city_from = [0] * city_edges
    city_to = [0] * city_edges

    for i in range(city_edges):
        city_from[i], city_to[i] = map(int, input().rstrip().split())

    company = int(input().strip())

    result = order(city_nodes, city_from, city_to, company)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()

"""

STDIN     Function
-----     --------
5 5   →   cityNodes = 5, n = 5
1 2   →   cityFrom = 1, cityTo = 2
1 3   →   cityFrom = 1, cityTo = 3
2 4   →   cityFrom = 2, cityTo = 4
3 5   →   cityFrom = 3, cityTo = 5
1 5   →   cityFrom = 1, cityTo = 5
1     →   company = 1


Same input
5 5
1 2
1 3
2 4
3 5
1 5
1  
"""

"""
STDIN     Function
-----     --------
3 1   →   cityNodes = 3, n = 1
1 2   →   cityFrom = 1, cityTo = 2
2     →   company = 2


3 1
1 2
2  
"""
