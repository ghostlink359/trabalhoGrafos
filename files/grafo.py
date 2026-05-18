class Grafo:
    def __init__(self):
        # conjunto de vértices (não repete)
        self.vertices = set()
        # lista de arestas (tuplas)
        self.arestas = []

    def adicionar_aresta(self, u, v):
        """
        Adiciona uma aresta ao grafo
        """
        self.vertices.add(u)
        self.vertices.add(v)
        self.arestas.append((u, v))

    def mostrar(self):
        """
        Exibe o grafo
        """
        print("Vértices:", self.vertices)
        print("Arestas:", self.arestas)

    def limpar(self):
        """
        Reseta o grafo
        """
        self.vertices.clear()
        self.arestas.clear()