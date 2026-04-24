# Coloração de Grafos com DSatur — Mapa do Brasil
Modelagem do mapa político do Brasil como grafo não direcionado e aplicação do algoritmo DSatur.

---

## Apresentação
🔗 **[Assista à apresentação do trabalho aqui](link-do-video)**

---

## Sobre o projeto
O programa modela os 26 estados e o Distrito Federal do Brasil como um grafo não-direcionado, onde **cada vértice representa um estado** e **cada aresta representa uma fronteira** terrestre entre dois estados. O algoritmo **DSatur** colore os vértices de forma que nenhum par de estados vizinhos compartilhe a mesma cor, minimizando o número de cores utilizadas.

---

## Estrutura do projeto
```
trabalho-coloracao-grafo/
├── README.md
├── dsatur.md
├── dados/
│   └── brasil.txt
└── src/
    ├── main.py
    ├── graph.py
    └── dsatur.py
```

---

## Como executar
**Requisitos:** Python 3.10+ — nenhuma biblioteca externa necessária.
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/trabalho-coloracao-grafo.git
cd trabalho-coloracao-grafo/src

# Executar com o arquivo de dados
python3 main.py ../dados/brasil.txt
```

---

## Referência
Estrutura e nomenclatura baseadas na biblioteca [algs4](https://algs4.cs.princeton.edu/home/) de Sedgewick & Wayne.
