from grafo import Grafo

def camino_hamiltoniano(grafo:Grafo):
    visitados = set()
    
    for vertice in grafo:
        camino = _camino_hamiltoniano(grafo, vertice, visitados, [])
        if camino is not None:
            return camino
    
    return None

def _camino_hamiltoniano(grafo, vertice, visitados, camino_actual):
    visitados.add(vertice)
    camino_actual.append(vertice)
    
    if len(camino_actual) == len(grafo):
        return camino_actual
    
    for ady in grafo.adyacentes(vertice):
        if ady in visitados:
            continue
        resultado = _camino_hamiltoniano(grafo, ady, visitados, camino_actual)
        if resultado is not None:
            return resultado
    
    visitados.remove(vertice)
    camino_actual.pop()
    return None

grafo = Grafo()
grafo.agregar_vertice("asd")
print(camino_hamiltoniano(grafo))