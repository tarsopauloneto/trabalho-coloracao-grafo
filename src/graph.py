class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def adjacents(self, v):
        return self.adj[v]

    def degree(self, v):
        return len(self.adj[v])

    def __str__(self):
        result = ""
        for v in range(self.V):
            result += f"{v}: {' '.join(map(str, self.adj[v]))}\n"
        return result
