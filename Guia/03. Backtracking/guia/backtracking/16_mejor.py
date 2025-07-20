from grafo import Grafo

def pintar_colectivos(colectivos, paradas):
    grafo = armar_grafo(colectivos, paradas)
    vertices = grafo.obtener_vertices()

    colores = {}

    for i in range(len(vertices)):
        colores[vertices[i]] = i
    
    k_max = _pintar_colectivos(grafo, vertices, 0, colores, 0, len(vertices))
    return k_max

def _pintar_colectivos(grafo, vertices, actual, colores, k_parcial, k_max):
    # Poda 1: Si el ultimo que agregue no cumple, vuelvo
    if not ultimo_cumple(grafo, vertices, colores, actual):
        return k_max
    
    if actual == len(vertices):
        if k_parcial < k_max:
            return k_parcial
        return k_max
    
    # Poda 2: Si ya use mas colores que la mejor sol, vuelvo
    if k_parcial >= k_max:
        return k_max
    
    colectivo = vertices[actual]
    mejor_k = k_max

    for i in range(len(vertices)):
        colores[colectivo] = i
        if i > k_parcial:
            k_parcial = i
        mejor_k = _pintar_colectivos(grafo, vertices, actual+1, colores, k_parcial, mejor_k)
    
    del colores[colectivo]
    return mejor_k
        

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
                if not grafo.estan_unidos(parada[i], parada[j]):
                    grafo.agregar_arista(parada[i], parada[j])
    
    return grafo

print(pintar_colectivos([1,2,3,4,5,6,7,8], [[1,2,3,4], [5,6,7,8]]))