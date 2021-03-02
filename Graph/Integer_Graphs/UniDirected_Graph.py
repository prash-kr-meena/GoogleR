from Utils.Matrix import get_filled_matrix, print_matrix
# First networkx library is imported along with matplotlib
import networkx as nx
import matplotlib.pyplot as plt


class UniDirectedGraph:
    CONNECTED = 1
    NOT_CONNECTED = 0
    VISITED = True
    UN_VISITED = False

    def __init__(self):
        self.vertices = int(input("V : "))  # No of Vertices
        self.edges = int(input("E : "))  # # No of Edges

        self.edge_pairs: list[tuple] = []  # list of edge pairs
        self.adj_matrix = get_filled_matrix(self.vertices + 1, self.vertices + 1, UniDirectedGraph.NOT_CONNECTED)
        # we are adding 2 extra, row & columns, so that we can work easily with 0 based graph as well as 1 based graphs

        for i in range(self.edges):
            edge_from, edge_to = map(int, input().strip().split())
            self.edge_pairs.append((edge_from, edge_to))
            self.adj_matrix[edge_from][edge_to] = UniDirectedGraph.CONNECTED  # uni-directional  Notice

    def print_depth_first(self):
        print("\nPrint DFS : ")
        n = len(self.adj_matrix)

        # Notice : To handle dis-connected components : make sure to visit every node
        visited = [UniDirectedGraph.UN_VISITED] * n  # Array : to check if already visited in O(1)

        for vertex, status in enumerate(visited):
            if status == UniDirectedGraph.UN_VISITED:
                self._print_dfs(vertex, visited)
        print()

    def _print_dfs(self, start_vertex, visited: list):
        n = len(self.adj_matrix)

        print(start_vertex, end=" ")
        visited[start_vertex] = UniDirectedGraph.VISITED  # marking visited

        for i in range(n):
            for j in range(n):
                if self.adj_matrix[i][j] == UniDirectedGraph.CONNECTED and visited[j] == UniDirectedGraph.UN_VISITED:
                    # vertex i & j are connected and vertex j is not visited
                    self._print_dfs(j, visited)
                # else : continue

    def print_breadth_first(self):
        print("\nPrint BFS : ")
        pass

    def draw(self):
        graph = nx.DiGraph()
        graph.add_edges_from(self.edge_pairs)
        pos = nx.spring_layout(graph)
        plt.figure()
        nx.draw_networkx(graph, pos, edge_color='black', width=2, linewidths=4,
                         node_size=500, node_color='pink', alpha=1)
        plt.axis('off')
        plt.show()


if __name__ == '__main__':
    undirected_graph = UniDirectedGraph()
    # print_matrix(undirected_graph.adj_matrix)
    undirected_graph.print_depth_first()
    undirected_graph.draw()

"""
    2 <--- 1 ---> 3

3
2
1 2
1 3
"""

"""
    2 <--- 1 ---> 3           4 <-- 5

5
3
1 2
1 3
4 5
"""
