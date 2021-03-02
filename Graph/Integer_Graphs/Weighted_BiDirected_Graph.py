from collections import deque

from Utils.Matrix import get_filled_matrix, print_matrix
# First networkx library is imported along with matplotlib
import networkx as nx
import matplotlib.pyplot as plt


class WeightedBiDirectedGraph:
    CONNECTED = 1
    NOT_CONNECTED = 0
    VISITED = True
    UN_VISITED = False

    def __init__(self):
        self.vertices = int(input("V : "))  # No of Vertices
        self.edges = int(input("E : "))  # # No of Edges

        self.edge_pairs: list[tuple] = []  # list of edge pairs (from, to, weight)
        self.adj_matrix = get_filled_matrix(self.vertices + 1, self.vertices + 1, WeightedBiDirectedGraph.NOT_CONNECTED)

        for i in range(self.edges):
            edge_from, edge_to, edge_weight = map(int, input().strip().split())
            self.edge_pairs.append((edge_from, edge_to, edge_weight))
            self.adj_matrix[edge_from][edge_to] = WeightedBiDirectedGraph.CONNECTED
            self.adj_matrix[edge_to][edge_from] = WeightedBiDirectedGraph.CONNECTED  # Bi-directional Notice

    def print_depth_first(self):
        print("\nPrint DFS : ")
        n = len(self.adj_matrix)

        # Notice : To handle dis-connected components : make sure to visit every node
        visited = [WeightedBiDirectedGraph.UN_VISITED] * n  # Array : to check if already visited in O(1)

        for vertex, status in enumerate(visited):
            if status == WeightedBiDirectedGraph.UN_VISITED:
                self._print_dfs(vertex, visited)
        print()

    def _print_dfs(self, start_vertex, visited: list):
        n = len(self.adj_matrix)

        print(start_vertex, end=" ")
        visited[start_vertex] = WeightedBiDirectedGraph.VISITED  # marking visited

        for i in range(n):
            for j in range(n):
                if self.adj_matrix[i][j] == WeightedBiDirectedGraph.CONNECTED \
                        and visited[j] == WeightedBiDirectedGraph.UN_VISITED:
                    # vertex i & j are connected and vertex j is not visited
                    self._print_dfs(j, visited)
                # else : continue

    def print_breadth_first(self):
        print("\nPrint BFS : ")
        n = len(self.adj_matrix)

        visited = [WeightedBiDirectedGraph.UN_VISITED] * n  # boolean array

        for vertex, status in enumerate(visited):
            if status == WeightedBiDirectedGraph.UN_VISITED:
                self._print_bfs(vertex, visited)
        print()

    def _print_bfs(self, vertex, visited):
        n = len(self.adj_matrix)

        queue = deque()
        queue.append(vertex)
        visited[vertex] = WeightedBiDirectedGraph.VISITED  # marking visited

        while len(queue) != 0:
            vertex_i = queue.popleft()

            print(vertex_i, end=" ")  # process

            for vertex_j in range(n):
                if self.adj_matrix[vertex_i][vertex_j] == WeightedBiDirectedGraph.CONNECTED \
                        and visited[vertex_j] == WeightedBiDirectedGraph.UN_VISITED:
                    # two vertices are adjacent, and not visited, so put all into queue to process later
                    queue.append(vertex_j)
                    visited[vertex_j] = WeightedBiDirectedGraph.VISITED

                    # to handle case, when the vertex is in queue, and you did not mark it visited and another vertex
                    # that you took out was connected to the one present in the queue, so it got pushed multiple times
                    # so when you push it to the queue mark it as visited, so no duplicates will appear in the queue

    def draw(self):
        graph = nx.Graph()

        only_edges = [(edge_from, edge_to) for edge_from, edge_to, weight in self.edge_pairs]
        graph.add_edges_from(only_edges)

        pos = nx.spring_layout(graph)
        plt.figure()
        nx.draw_networkx(graph, pos, edge_color='black', width=2, linewidths=4,
                         node_size=500, node_color='pink', alpha=1)
        # create edge label
        labels = {edge: pair[2] for edge, pair in zip(only_edges, self.edge_pairs)}
        # Draw edge labels according to node positions
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
        plt.axis('off')
        plt.show()


if __name__ == '__main__':
    weighted_bi_directed_graph = WeightedBiDirectedGraph()
    print_matrix(weighted_bi_directed_graph.adj_matrix)
    weighted_bi_directed_graph.print_depth_first()
    weighted_bi_directed_graph.print_breadth_first()
    weighted_bi_directed_graph.draw()

"""
    2 --9--  1 --0-- 3

3
2
1 2 9
1 3 1
"""

"""
    2 --9--  1  --0-- 3           4 --88-- 5

5
3
1 2 9
1 3 1
4 5 88
"""

"""
6
8
0 1 99
1 3 99
3 5 99
1 4 99
4 5 99
0 2 99
2 6 99
5 6 99
"""
