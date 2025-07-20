from grafo import Grafo

def hay_isomorfismo(g1:Grafo, g2:Grafo):
    # Casos base descartados
    if len(g1) != len(g2):
        return False
    
    # Diccionario del tipo cantidad_aristas: cant_vertices_con_esa_cant
    dicc_aristas_g1 = obtener_dicc_aristas(g1)
    dicc_aristas_g2 = obtener_dicc_aristas(g2)

    for cant_aristas in dicc_aristas_g1:
        if cant_aristas not in dicc_aristas_g2:
            return False
        
        if dicc_aristas_g1[cant_aristas] != dicc_aristas_g2[cant_aristas]:
            return False

    asignaciones = {}
    vertices_g1 = g1.obtener_vertices()
    vertices_g2 = set(g2.obtener_vertices())

    return _hay_isomorfismo(g1, g2, vertices_g1, vertices_g2, 0, asignaciones)

def _hay_isomorfismo(g1, g2, vertices_g1, restantes_g2, actual, asignaciones):
    if len(asignaciones) == len(vertices_g1):
        return True if ultimo_cumple(g1, g2, asignaciones, actual) else None
    
    # Poda
    if not ultimo_cumple(g1, g2, vertices_g1,asignaciones, actual):
        return None

    # No puedo iterar y borrar del set
    restantes = list(restantes_g2)
    actual_g1 = vertices_g1[actual]
    
    # Recorro los vertices restantes y pruebo cada asignación
    for vertice_g2 in restantes:
        asignaciones[actual_g1] = vertice_g2
        restantes_g2.remove(vertice_g2)

        resultado = _hay_isomorfismo(g1, g2, vertices_g1, restantes_g2, actual+1, asignaciones)
        if resultado is not None:
            return resultado
        
        del asignaciones[actual_g1]
        restantes_g2.add(vertice_g2)
    
    return None

def ultimo_cumple(g1, g2, vertices_g1, asignaciones, actual):
    if actual == 0:
        return True

    vertice_g1 = vertices_g1[actual-1]
    vertice_g2 = asignaciones[vertice_g1]

    if len(g1.adyacentes(vertice_g1)) != len(g2.adyacentes(vertice_g2)):
        return False

    for ady in g1.adyacentes(vertice_g1):
        if ady not in asignaciones:
            continue

        asignado_ady = asignaciones[ady]
        if asignado_ady not in g2.adyacentes(vertice_g2):
            return False
    
    return True

def obtener_dicc_aristas(grafo):
    dicc_aristas = {}

    for vertice in grafo:
        cant_aristas = len(grafo.adyacentes(vertice))
        if cant_aristas not in dicc_aristas:
            dicc_aristas[cant_aristas] = 0
        
        dicc_aristas[cant_aristas] += 1
    
    return dicc_aristas