from grafo import Grafo

def knight_tour(n):
    grafo = armar_grafo(n)
    resultado = _knight_tour(grafo, vertice, visitados, [])
    visitados = set()

    for vertice in grafo:
        resultado = _knight_tour(grafo, vertice, visitados, [])
        if resultado is not None:
            return resultado
    
    return None

def _knight_tour(grafo, vertice, visitados, cam_actual):
    visitados.add(vertice)
    cam_actual.append(vertice)
    
    if len(cam_actual) == len(grafo):
        return cam_actual

    for ady in grafo.adyacentes(vertice):
        if ady in visitados:
            continue
        # Si no esta visitado, voy con ese
        resultado = _knight_tour(grafo, ady, visitados, cam_actual)
        if resultado is not None:
            return resultado
    
    # No encontre camino valido con ningun mov. posible
    visitados.remove(vertice)
    cam_actual.pop()
    
    return None

def armar_grafo(n):
    grafo = Grafo()

    for i in range(n):
        for j in range(n):
            grafo.agregar_vertice((i, j))

    for i, j in grafo:
        aristas = [
            (i+2, j+1), (i+2, j-1), (i-2, j+1), (i-2, j-1),
            (i-1, j+2), (i-1, j-2), (i+1, j+2), (i+1, j-2)
        ]

        for k, m in aristas:
            if en_rango((k, m), n) and not grafo.estan_unidos((i, j), (k, m)):
                grafo.agregar_arista((i, j), (k, m))
    
    return grafo


def en_rango(posicion, n):
    i, j = posicion
    cond1 = i >= 0 and i < n
    cond2 = j >= 0 and j < n

    return cond1 and cond2