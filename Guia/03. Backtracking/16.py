from grafo import Grafo

def pintar_colectivos(colectivos, paradas):
    grafo = armar_grafo(colectivos, paradas)
    vertices = grafo.obtener_vertices()
    colores = {}    

    _colectivos(grafo, vertices, 0, colores)

    k_max = 0
    for colectivo in colores:
        if colores[colectivo] > k_max:
            k_max = colores[colectivo]
    
    return k_max+1

def _colectivos(grafo, vertices, actual, colores):
    if actual == len(vertices):
        if ultimo_cumple(grafo, vertices, colores, actual):
            return colores
        return None
    
    # Podas
    if not ultimo_cumple(grafo, vertices, colores, actual):
        return None
    
    colectivo = vertices[actual]

    solucion = None
    k = -1
    while solucion is None:
        k += 1
        colores[colectivo] = k
        solucion = _colectivos(grafo, vertices, actual+1, colores)
    
    return colores

def ultimo_cumple(grafo, vertices, colores, indice):
    if indice == 0:
        return True
    
    vertice = vertices[indice-1]
    color = colores[vertice]

    for ady in grafo.adyacentes(vertice):
        if ady in colores and colores[ady] == color:
            return False
    
    return True

def armar_grafo(colectivos, paradas):
    grafo = Grafo(vertices=colectivos)
    
    for parada in paradas:
        for i in range(len(parada)):
            for j in range(i+1, len(parada)):
                grafo.agregar_arista(parada[i], parada[j])
    
    return grafo

print(pintar_colectivos([1,2,3,4,5,6,7], [[1,2,3], [4,5,6], [5,6,7]]))