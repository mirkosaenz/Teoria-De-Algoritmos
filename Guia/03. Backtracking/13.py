from grafo import Grafo

def vertex_cover_min(grafo):
    vertices = grafo.obtener_vertices()
    aristas = obtener_aristas(grafo)

    solucion = _vertex_cover_min(vertices, 0, set() , set(vertices), aristas)

    return list(solucion)

def _vertex_cover_min(vertices, actual, sol_parcial, solucion, aristas):
    if actual == len(vertices):
        if cumple(sol_parcial, aristas):
            return sol_parcial.copy() # Despues saco para probar la otra opcion.
        return solucion
    
    # Poda
    if len(sol_parcial) >= len(solucion):
        return solucion
    
    min_vertex_cover = solucion
    
    # Busco sol agregandome 
    sol_parcial.add(vertices[actual])
    resultado = _vertex_cover_min(vertices, actual+1, sol_parcial, solucion)
    if len(resultado) < len(min_vertex_cover):
        min_vertex_cover = resultado
    
    # Busco sol sacandome
    sol_parcial.remove(vertices[actual])
    resultado = _vertex_cover_min(vertices, actual+1, sol_parcial, solucion)
    if len(resultado) < len(min_vertex_cover):
        min_vertex_cover = resultado

    # Retorno la mejor sol que encontre
    return min_vertex_cover

def cumple(grafo, sol_parcial, aristas):
    for arista in aristas:
        v, w = arista
        if v not in sol_parcial and w not in sol_parcial:
            return False
        
    return True

def obtener_aristas(grafo):
    aristas = set()
    for vertice in grafo:
        for ady in grafo.adyacentes(vertice):
            cond1 = (vertice, ady) not in aristas
            cond2 = (ady, vertice) not in aristas

            if cond1 and cond2:
                aristas.add((vertice, ady))
    
    return aristas