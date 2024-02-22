grafo = {
    'Brazil': [ 'Rio de Janeiro',  'São Paulo', 'Minas Gerais', 'Bahia',  'Ceará'],
    'Rio de Janeiro': [ 'Rio de Janeiro City','Niterói','Nova Iguaçu','Campos dos Goytacazes'],
    'São Paulo' : [ 'São Paulo City','Campinas','Guarulhos', 'Santos'], 
    'Minas Gerais': [ 'Belo Horizonte','Uberlândia','Contagem','Juiz de Fora'],
    'Bahia': [ 'Salvador','Feira de Santana','Vitória da Conquista'],
    'Ceará': [ 'Fortaleza', 'Caucaia', 'Juazeiro do Norte'],
    'Campos dos Goytacazes' : ['Campos City', 'São João da Barra', 'Itaperuna'],
    'Santos': ['Santos City', 'São Vicente', 'Praia Grande'],
    'Juiz de Fora': ['Juiz de Fora City', 'Muriaé', 'Cataguases']
}

def dfs(graph, start, target, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
        
    visited.add(start)
    path.append(start)

    if start == target:
        return True
    
    for next_node in graph.get(start, []):
        if next_node not in visited:
            if dfs(graph, next_node,target, visited, path):
                return path
     
    return False

print("Caminho percorrido: ")
if dfs(grafo, 'São Paulo', 'Feira de Santana') == False: 
    print('Impossivel chegar')
