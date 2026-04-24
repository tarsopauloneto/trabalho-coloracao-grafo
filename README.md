# Coloração de Grafos com DSatur — Mapa do Brasil

Modelagem do mapa político do Brasil como grafo não direcionado e aplicação do algoritmo **DSatur**.

---

## 🎥 Apresentação

🔗 **[Assista à apresentação do trabalho aqui](link-do-video)**

---

## 📌 Sobre o projeto

- Cada vértice → estado brasileiro
- Cada aresta → fronteira terrestre
- O algoritmo DSatur colore o grafo minimizando conflitos

---

## 📂 Estrutura

trabalho-coloracao-grafo/
├── README.md
├── dsatur.md
├── dados/
│ └── brasil.txt
└── src/
├── main.py
├── graph.py
└── dsatur.py

---

## ▶️ Execução

```bash
cd src
python3 main.py ../dados/brasil.txt
```
