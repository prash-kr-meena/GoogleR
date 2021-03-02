from Utils.Matrix import get_filled_matrix, print_matrix
# First networkx library is imported along with matplotlib
import networkx as nx
import matplotlib.pyplot as plt


class BiDirectedGraph:
    CONNECTED = 1
    NOT_CONNECTED = 0
    VISITED = True
    UN_VISITED = False

    def __init__(self):
        self.vertices = int(input("V : "))  # No of Vertices
        self.edges = int(input("E : "))  # # No of Edges

        self.edge_pairs: list[tuple] = []  # list of edge pairs
        self.adj_matrix = get_filled_matrix(self.vertices + 1, self.vertices + 1, BiDirectedGraph.NOT_CONNECTED)
        # we are adding 2 extra, row & columns, so that we can work easily with 0 based graph as well as 1 based graphs

        for i in range(self.edges):
            edge_from, edge_to = map(int, input().strip().split())
            self.edge_pairs.append((edge_from, edge_to))
            self.adj_matrix[edge_from][edge_to] = BiDirectedGraph.CONNECTED
            self.adj_matrix[edge_to][edge_from] = BiDirectedGraph.CONNECTED  # making bi-directed-graphs

    def draw(self):
        graph = nx.Graph()
        graph.add_edges_from(self.edge_pairs)
        nx.draw_networkx(graph)
        plt.show()

    def print_depth_first(self):
        print("\nPrint DFS : ")
        n = len(self.adj_matrix)

        # Notice : To handle dis-connected components : make sure to visit every node
        visited = [BiDirectedGraph.UN_VISITED] * n  # Array : to check if already visited in O(1)

        for vertex, status in enumerate(visited):
            if status == BiDirectedGraph.UN_VISITED:
                self._print_dfs(vertex, visited)

    def _print_dfs(self, start_vertex, visited: list):
        n = len(self.adj_matrix)

        print(start_vertex, end=" ")
        visited[start_vertex] = BiDirectedGraph.VISITED  # marking visited

        for i in range(n):
            for j in range(n):
                if self.adj_matrix[i][j] == BiDirectedGraph.CONNECTED and visited[j] == BiDirectedGraph.UN_VISITED:
                    # vertex i & j are connected and vertex j is not visited
                    self._print_dfs(j, visited)
                # else : continue

    def print_breadth_first(self):
        print("\nPrint BFS : ")
        pass


if __name__ == '__main__':
    undirected_graph = BiDirectedGraph()
    print_matrix(undirected_graph.adj_matrix)
    undirected_graph.print_depth_first()
    undirected_graph.draw()

"""
    2 --- 1 --- 3

3
2
1 2
1 3
"""

"""
    2 --- 1 --- 3           4 -- 5

5
3
1 2
1 3
4 5
"""
