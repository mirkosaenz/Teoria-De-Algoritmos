from grafo import Grafo

def independent_set(grafo:Grafo):
    vertices = grafo.obtener_vertices()
    resultado = []

    for i in range(len(vertices)):
        res_actual = _independent_set(grafo, vertices, i, [], resultado)
        
        if res_actual != None:
            if len(res_actual) > len(resultado):
                resultado = res_actual
    
    return resultado

def _independent_set(grafo, vertices, actual, res_parcial, sol_actual):
    # Si llegue al final, devuelvo el resultado o None si no mejore
    if actual == len(vertices):
        if ultimo_cumple(grafo, res_parcial):
            return res_parcial.copy() if len(res_parcial) > len(sol_actual) else None
    
    # PODA: Checkeo si el ultimo cumple, sino retorno
    if not ultimo_cumple(grafo, res_parcial):
        return None
    
    res_parcial.append(vertices[actual])

    resultado = _independent_set(grafo, vertices, actual+1, res_parcial, sol_actual)
    if resultado != None:
        sol_actual = resultado
    
    res_parcial.pop()
    resultado = _independent_set(grafo, vertices, actual+1, res_parcial, sol_actual)
    if resultado != None:
        sol_actual = resultado
    
    return sol_actual

def ultimo_cumple(grafo, res_parcial):
    if len(res_parcial) == 0:
        return True
    
    ultimo = res_parcial[len(res_parcial)-1]
    for vertice in res_parcial:
        if vertice == ultimo:
            continue
        if vertice in grafo.adyacentes(ultimo):
            return False
        
    return True

def probar_ind_set():
    vertices = [1,2,3,4,5,6]
    grafo = Grafo(es_dirigido=False, vertices=vertices)
    grafo.agregar_arista(1,2)

    print(independent_set(grafo))

probar_ind_set()