import sys
from graph import Graph
from dsatur import DSatur

SIGLAS = [
    "AC","AL","AM","AP","BA","CE","DF","ES","GO","MA",
    "MG","MS","MT","PA","PB","PE","PI","PR","RJ","RN",
    "RO","RR","RS","SC","SE","SP","TO"
]

def read_graph(path):
    with open(path) as f:
        V = int(f.readline())
        E = int(f.readline())

        g = Graph(V)

        for _ in range(E):
            v, w = map(int, f.readline().split())
            g.add_edge(v, w)

    return g

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <arquivo>")
        return

    g = read_graph(sys.argv[1])

    print("=== Lista de Adjacência ===")
    print(g)

    ds = DSatur(g)
    colors = ds.run()

    print("\n=== Ordem de Coloração ===")
    print([SIGLAS[v] for v in ds.order])

    print("\n=== Cores ===")
    for v in range(g.V):
        print(f"{SIGLAS[v]} -> Cor {colors[v]}")

    print("\nTotal de cores:", max(colors) + 1)

    print("\nColoração válida:", "Sim" if ds.is_valid() else "Não")

if __name__ == "__main__":
    main()
