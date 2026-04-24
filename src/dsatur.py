class DSatur:
    def __init__(self, graph):
        self.graph = graph
        self.V = graph.V
        self.colors = [-1] * self.V
        self.order = []

    def saturation_degree(self, v):
        colors = set()
        for u in self.graph.adjacents(v):
            if self.colors[u] != -1:
                colors.add(self.colors[u])
        return len(colors)

    def get_next_vertex(self):
        max_sat = -1
        candidates = []

        for v in range(self.V):
            if self.colors[v] == -1:
                sat = self.saturation_degree(v)

                if sat > max_sat:
                    max_sat = sat
                    candidates = [v]
                elif sat == max_sat:
                    candidates.append(v)

        return max(candidates, key=lambda v: self.graph.degree(v))

    def get_color(self, v):
        used = set()
        for u in self.graph.adjacents(v):
            if self.colors[u] != -1:
                used.add(self.colors[u])

        color = 0
        while color in used:
            color += 1
        return color

    def run(self):
        # começa com maior grau
        start = max(range(self.V), key=lambda v: self.graph.degree(v))
        self.colors[start] = 0
        self.order.append(start)

        for _ in range(self.V - 1):
            v = self.get_next_vertex()
            color = self.get_color(v)
            self.colors[v] = color
            self.order.append(v)

        return self.colors

    def is_valid(self):
        for v in range(self.V):
            for u in self.graph.adjacents(v):
                if self.colors[v] == self.colors[u]:
                    return False
        return True
