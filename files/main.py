from grafo import Grafo
from vertex_cover import vertex_cover_aproximado
from interface import exibir_menu, exibir_resultado


def menu():
    print("\n=== WAR ROOM ===")
    print("1 - Adicionar aresta")
    print("2 - Carregar grafo de arquivo")
    print("3 - Mostrar grafo")
    print("4 - Resolver Vertex Cover")
    print("5 - Sair")


def carregar_arquivo(nome_arquivo, grafo):
    try:
        with open(f"exemplos/{nome_arquivo}", "r") as f:
            for linha in f:
                u, v = linha.strip().split()
                grafo.adicionar_aresta(u, v)
        print("Grafo carregado com sucesso!")
    except Exception as e:
        print("Erro ao carregar arquivo:", e)


def mostrar_grafo(grafo):
    print("\n=== GRAFO ===")
    print("Vértices:", grafo.vertices)
    print("Arestas:", grafo.arestas)


def resolver_vertex_cover(grafo):
    if not grafo.arestas:
        print("Grafo vazio!")
        return

    resultado = vertex_cover_aproximado(grafo.arestas)

    print("\n=== RESULTADO ===")
    print("Cobertura:", resultado)
    print("Tamanho:", len(resultado))


def main():
    g = Grafo()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            u = input("Vértice 1: ")
            v = input("Vértice 2: ")
            g.adicionar_aresta(u, v)

        elif opcao == "2":
            nome = input("Nome do arquivo (ex: grafo1.txt): ")
            carregar_arquivo(nome, g)

        elif opcao == "3":
            mostrar_grafo(g)

        elif opcao == "4":
            resolver_vertex_cover(g)

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()