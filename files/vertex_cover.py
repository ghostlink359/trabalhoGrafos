def vertex_cover_aproximado(arestas):
    cobertura = set()
    arestas_restantes = arestas.copy()

    while arestas_restantes:
        # pega uma aresta qualquer
        u, v = arestas_restantes.pop()

        # adiciona os dois vértices na cobertura
        cobertura.add(u)
        cobertura.add(v)

        # remove todas as arestas cobertas por u ou v
        novas_arestas = []
        for a, b in arestas_restantes:
            if u not in (a, b) and v not in (a, b):
                novas_arestas.append((a, b))

        arestas_restantes = novas_arestas

    return cobertura