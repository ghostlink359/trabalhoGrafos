# trabalhoGrafos

### Descrição

Este projeto foi desenvolvido para a disciplina de Estruturas, Pesquisar e Ordenação de Dados com o objetivo de simular um cenário de War Room, onde uma rede de dispositivos é analisada utilizando grafos.

### Integrantes

- Patrick Guilherme
- Gabriel da Silva 
- Matheus Nogueira

### Funcionalidades

- Representação de grafos (vértices e arestas)
- Inserção manual de arestas
- Leitura de grafos a partir de arquivos .txt
- Execução do algoritmo de Vertex Cover

Exibição de:

- vértices escolhidos
- tamanho da cobertura

### Estrutura do Projeto|

```bash
TRABALHOGRAFOS/
│
├── exemplos/
│   ├── grafo1.txt
│   └── grafo2.txt
│
├── files/
│   ├── grafo.py
│   ├── vertex_cover.py
│   ├── interface.py
│   └── __init__.py
│
├── main.py
├── README.md
└── relatorio.pdf
```

### Como executar
Abra o terminal na pasta do projeto

Execute:

```bash
python main.py
```

### Complexidade
O problema exato de Vertex Cover é NP-Completo

O algoritmo utilizado possui complexidade aproximada:

O(E²)
Onde E é o número de arestas do grafo.