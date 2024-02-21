from collections import deque


grafo = {
    'Uberlândia': {'Araguari', 'Tupaciguara', 'Monte Alegre de Minas', 'Uberaba'},
    'Araguari': {'Uberlândia', 'Tupaciguara', 'Monte Carmelo'},
    'Tupaciguara': {'Uberlândia', 'Araguari', 'Monte Alegre de Minas'},
    'Monte Alegre de Minas': {'Uberlândia', 'Tupaciguara'},
    'Monte Carmelo': {'Uberlândia', 'Araguari'},
    'Uberaba': {'Uberlândia', 'Delta', 'Igarapava'}
}


def imprimir_arvore(grafo, raiz):
    fila = deque([raiz])
    visitados = set()

    while fila:
        vertice = fila.popleft()
        if vertice not in visitados:
            print(f'{vertice}:')
            visitados.add(vertice)
            vizinhos = grafo.get(vertice, set())
            for vizinho in vizinhos:
                if vizinho not in visitados:
                    print(f"\t{vizinho}")
                    fila.append(vizinho)
            print(50 * '-')

imprimir_arvore(grafo, 'Uberlândia')
