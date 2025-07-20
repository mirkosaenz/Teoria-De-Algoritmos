import collections

def es_bipartito(grafo):
    visitados = set()
    for vertice in grafo:
        if vertice not in visitados:
            visitados.add(vertice)
            colores = colorear(grafo, vertice, visitados)

    for vertice in grafo:
        for ady in grafo.adyacentes(vertice):
            if colores[ady] == colores[vertice]:
                return False
            
    return True

def colorear(grafo, vertice, visitados):
    cola = collections.deque()
    colores = {}
    
    colores[vertice] = 1
    cola.append(vertice)

    while len(cola) != 0:
        actual = cola.popleft()
        visitados.add(actual)
        
        for ady in grafo.adyacentes(actual):
            if ady not in visitados:
                colores[ady] = 1-colores[actual]
                cola.append(ady)

    return colores