class Graph:
    def __init__(self, v_count) -> None:
        self.vertext_count = v_count
        self.adj_matrix = [[0] * v_count for _ in range(v_count)]

    def add_edge(self, u, v, weight=1):
        if 0 <= u < self.vertext_count and 0 <= v < self.vertext_count:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
        else:
            print("Invalid Vertices")

    def remove_edge(self, u, v):
        if 0 <= u < self.vertext_count and 0 <= v < self.vertext_count:
            self.adj_matrix[u][v] = 0
            self.adj_matrix[v][u] = 0
        else:
            print("Invalid Vertices")

    def has_edge(self, u, v):
        if 0 <= u < self.vertext_count and 0 <= v < self.vertext_count:
            return self.adj_matrix[u][v] != 0 and self.adj_matrix[v][u] != 0
        else:
            print("Invalid Vertices")

    def print_adj_matrix(self):
        for row_lst in self.adj_matrix:
            # print(" ".join(map(str, row_lst)))
            print([a for a in row_lst])


# driver code
g = Graph(4)
g.add_edge(1, 0, 2)
g.add_edge(0, 2, 1)
g.add_edge(2, 1, 1)
g.add_edge(1, 2, 2)
g.add_edge(3, 2, 5)
print(f"Has edge from {2} to {1}: {g.has_edge(2, 1)}")
print(f"Has edge from {0} to {3}: {g.has_edge(0, 3)}")
g.print_adj_matrix()
