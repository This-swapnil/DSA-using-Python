class Graph:
    def __init__(self, v_count) -> None:
        self.vertext_count = v_count
        self.adj_list = {v: [] for v in range(v_count)}  # {0: [], 1: [], 2: [], 3: []}

    def add_edge(self, u, v, weight=1):
        if 0 <= u < self.vertext_count and 0 <= v < self.vertext_count:
            self.adj_list[u].append((v, weight))
            self.adj_list[v].append((u, weight))
        else:
            print("Invalid Vertices")

    def remove_edge(self, u, v):
        if 0 <= u < self.vertext_count and 0 <= v < self.vertext_count:
            self.adj_list[u] = [
                (vertex, weight) for vertex, weight in self.adj_list[u] if vertex != v
            ]
            self.adj_list[v] = [
                (vertex, weight) for vertex, weight in self.adj_list[v] if vertex != u
            ]
        else:
            print("Invalid Vertices")

    def has_edge(self, u, v):
        if 0 <= u < self.vertext_count and 0 <= v < self.vertext_count:
            return any(vertex == v for vertex, _ in self.adj_list[u])
        else:
            print("Invalid Vertices")
            return False

    def print_adj_list(self):
        for vertex, n in self.adj_list.items():
            print(f"V,{vertex},:,{n}")


# Driver code
g = Graph(4)
g.add_edge(1, 0)
g.add_edge(0, 2)
g.add_edge(2, 1)
g.add_edge(1, 2)
g.add_edge(3, 2)
print(f"Has edge from {2} to {1}: {g.has_edge(2, 1)}")
print(f"Has edge from {0} to {3}: {g.has_edge(0, 3)}")
g.print_adj_list()
