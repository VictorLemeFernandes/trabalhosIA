# O grafo é representado como um dicionário. As chaves são os nós do grafo e os valores associados a cada chave são listas de nós adjacentes. Por exemplo, para o nó 'Minas Gerais', a lista associada inclui suas cidades vizinhas como 'Belo Horizonte', 'Uberlândia', 'Contagem' e 'Juiz de Fora'.

grafo = {
    'Brazil': [ 'Rio de Janeiro',  'São Paulo', 'Minas Gerais', 'Bahia',  'Ceará'],
    'Rio de Janeiro': [ 'Rio de Janeiro City','Niterói','Nova Iguaçu','Campos dos Goytacazes'],
    'São Paulo' : [ 'São Paulo City','Campinas','Guarulhos', 'Santos'], 
    'Minas Gerais': [ 'Belo Horizonte','Uberlândia','Contagem','Juiz de Fora'],
    'Bahia': [ 'Salvador','Feira de Santana','Vitória da Conquista'],
    'Ceará': [ 'Fortaleza', 'Caucaia', 'Juazeiro do Norte'],
    'Campos dos Goytacazes' : ['Campos City', 'São João da Barra', 'Itaperuna'],
    'Santos': ['Santos City', 'São Vicente', 'Praia Grande'],
    'Juiz de Fora': ['Juiz de Fora City', 'Muriaé', 'Cataguases'],
    'Uberlândia': ['Uberaba', 'Araguari'],
    'Uberaba': ['Igarapava', 'Delta', 'Conceição das Alagoas']
}

# Pq usamos um dicionario:
# O acesso aos vizinhos de um nó é rápido
# Facilidade de implementacao
# Clareza e legibilidade

def dfs(graph, start, target, visited=None, path=None):
    # Se a lista de nós visitados não foi inicializada, inicialize-a como um conjunto vazio.
    if visited is None:
        visited = set()
    # Se a lista de caminho não foi inicializada, inicialize-a como uma lista vazia.
    if path is None:
        path = []
    
    # Adiciona o nó atual à lista de visitados.
    visited.add(start)
    # Adiciona o nó atual ao caminho percorrido.
    path.append(start)

    # Se o nó atual for o nó alvo, retorna o caminho percorrido.
    if start == target:
        return True
    
    # Para cada nó adjacente ao nó atual...
    for next_node in graph.get(start, []):
        # Se o nó adjacente não foi visitado ainda...
        if next_node not in visited:
            # Chama recursivamente a DFS a partir do nó adjacente.
            if dfs(graph, next_node,target, visited, path):
                return path
            
    # Se o nó alvo não for encontrado em nenhum caminho possível, retorna False.
    return False

print("Caminho percorrido:")
# Chama a função DFS para encontrar um caminho de 'Minas Gerais' até 'Juiz de Fora City'.
path = dfs(grafo, 'Brazil', 'Araguari')
# Se um caminho for encontrado, imprime-o.
if path != False:
    print('Numero de lugares visitados:', len(path))
    print(path)
# Caso contrário, imprime que é impossível chegar.
else:
    print('Impossível chegar')