from grafo import Grafo

def dominating_set_min(grafo):
    vertices = grafo.obtener_vertices()
    restantes = set(vertices)

    return _dominating_set(grafo, vertices, 0, restantes, [], vertices, [])

def _dominating_set(grafo, vertices, actual, restantes, sol_parcial, sol_actual, sacados):
    if actual == len(vertices):
        if ultimo_necesario(sol_parcial, restantes) and len(sol_parcial) < len(sol_actual):
            # Despues voy a borrar para probar la otra opción
            return sol_parcial.copy() if cumple(grafo, sol_parcial) else sol_actual
        return sol_actual
    
    #PODAS
    # Si ya cumplia y me agregue igual, no hay mejor sol por aca
    if not ultimo_necesario(sol_parcial, restantes):
        return sol_actual
    
    # Si la sol parcial ya es peor que la actual, vuelvo
    if len(sol_parcial) >= len(sol_actual):
        return sol_actual
    
    # Si saque un vertice sin adyacentes, vuelvo
    if saque_necesario(grafo, sacados):
        return sol_actual
    
    min_dom_set = sol_actual
    
    # Pruebo agregandome
    sol_parcial.append(vertices[actual])
    sacar_adyacentes(grafo, restantes, vertices[actual])
    resultado = _dominating_set(grafo, vertices, actual+1, restantes, sol_parcial, sol_actual, sacados)
    if len(resultado) < len(min_dom_set):
        min_dom_set = resultado
    
    # Pruebo sacandome
    sol_parcial.pop()
    sacados.append(vertices[actual])
    agregar_adyacentes(grafo, restantes, vertices[actual])
    resultado = _dominating_set(grafo, vertices, actual+1, restantes, sol_parcial, sol_actual, sacados)
    if len(resultado) < len(min_dom_set):
        min_dom_set = resultado

    sacados.pop()
    
    return min_dom_set

def saque_necesario(grafo, sacados):
    if len(sacados) == 0:
        return False
    
    ultimo = sacados[len(sacados)-1]
    return len(grafo.adyacentes(ultimo)) == 0

def cumple(grafo, subconjunto):
    subconjunto = set(subconjunto)

    for vertice in grafo:
        if vertice in subconjunto:
            continue

        cumple = False
        for vertice_subc in subconjunto:
            if vertice in grafo.adyacentes(vertice_subc):
                cumple = True
                break
        
        if not cumple:
            return False
    
    return True

def ultimo_necesario(sol_parcial, restantes):
    if len(sol_parcial) == 0:
        return True
    
    ultimo = sol_parcial[len(sol_parcial)-1]
    return ultimo in restantes

def sacar_adyacentes(grafo, restantes, vertice):
    for ady in grafo.adyacentes(vertice):
        if ady in restantes:
            restantes.remove(ady)

def agregar_adyacentes(grafo, restantes, vertice):
    for ady in grafo.adyacentes(vertice):
        if ady not in restantes:
            restantes.add(ady)