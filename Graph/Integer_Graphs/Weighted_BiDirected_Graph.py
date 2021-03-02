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
        pass

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
    undirected_graph = WeightedBiDirectedGraph()
    print_matrix(undirected_graph.adj_matrix)
    undirected_graph.print_depth_first()
    undirected_graph.draw()

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
