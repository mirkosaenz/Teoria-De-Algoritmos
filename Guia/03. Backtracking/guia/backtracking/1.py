from grafo import Grafo

def no_adyacentes(grafo:Grafo, n):
    'Devolver una lista con los n vértices, o None de no ser posible'

    vertices = grafo.obtener_vertices()
    for i in range(len(vertices)):
        resultado = _no_adyacentes(grafo, list(vertices), i, [], n)

        if resultado is not None:
            return resultado
    
    return None

def _no_adyacentes(grafo, vertices, actual, subconjunto, n):
    if len(subconjunto) == n:
        return subconjunto if ultimo_cumple(grafo, subconjunto) else None
    
    if actual == len(vertices):
        return None
    
    # Podas
    cond1 = not ultimo_cumple(grafo, subconjunto)
    cond2 = not quedan_suficientes(n, subconjunto, vertices, actual)
    if cond1 or cond2:
        return None
    
    subconjunto.append(vertices[actual])

    # Pruebo si hay alguna combinacion posible incluyendome
    resultado = _no_adyacentes(grafo, vertices, actual+1, subconjunto, n)
    if resultado is not None:
        return resultado
    
    # Pruebo si hay alguna combinacion posible sin incluirme
    subconjunto.pop()
    return _no_adyacentes(grafo, vertices, actual+1, subconjunto, n)

def ultimo_cumple(grafo, subconjunto):
    if len(subconjunto) == 0:
        return True
    
    ultimo = subconjunto[len(subconjunto)-1]
    
    for v in subconjunto:
        if v == ultimo:
            continue
        if v in grafo.adyacentes(ultimo):
            return False
    
    return True

def quedan_suficientes(n, subconjunto, vertices, actual):
    # Importante: si llame con actual, es pq todavia no puse ese indice
    # --> actual indica la cant de elementos anteriores (los que ya no puedo poner)
    return (n - len(subconjunto)) <= len(vertices) - actual 

grafo = Grafo(es_dirigido=False, vertices=["A", "B","C", "D", "E"])
print(no_adyacentes(grafo, 4))