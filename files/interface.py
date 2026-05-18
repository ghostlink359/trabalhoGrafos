def exibir_menu():
    print("\n=== WAR ROOM ===")
    print("1 - Adicionar aresta")
    print("2 - Carregar grafo de arquivo")
    print("3 - Mostrar grafo")
    print("4 - Resolver Vertex Cover")
    print("5 - Sair")


def exibir_resultado(cobertura):
    print("\n=== RESULTADO ===")
    print("Cobertura:", cobertura)
    print("Tamanho:", len(cobertura))