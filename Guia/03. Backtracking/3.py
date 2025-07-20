from grafo import Grafo

def nreinas(n):
    grafo = armar_grafo(n)
    vertices = grafo.obtener_vertices()

    for i in range(len(vertices)):
        resultado = _n_reinas(grafo, vertices, i, n, [])
        if resultado != None:
            return grafo, resultado
        
    return grafo, None

def _n_reinas(grafo, vertices, actual, n, res_parcial):
    if len(res_parcial) == n:
        return res_parcial if ultimo_cumple(grafo, res_parcial) else None
    
    if actual == len(vertices):
        return None
    
    if not ultimo_cumple(grafo, res_parcial):
        return None
    
    vertice_actual = vertices[actual]
    res_parcial.append(vertice_actual)

    resultado = _n_reinas(grafo, vertices, actual+1, n, res_parcial)
    if resultado != None:
        return resultado
    
    res_parcial.pop()
    return _n_reinas(grafo, vertices, actual+1, n, res_parcial)

def ultimo_cumple(grafo, res_parcial):
    if len(res_parcial) == 0:
        return True
    
    vertice = res_parcial[len(res_parcial)-1]

    for w in res_parcial:
        if w == vertice:
            continue
        if w in grafo.adyacentes(vertice):
            return False
    
    return True

def armar_grafo(n):
    grafo = Grafo(es_dirigido=False)

    # Agrego vertices al grafo
    for i in range(n):
        for j in range(n):
            grafo.agregar_vertice((i, j))
    
    # Agrego aristas a las posiciones donde la reina podria comer
    for (i, j) in grafo.obtener_vertices():
        
        # Agrego aristas a la fila
        for columna in range(n):
            if (i, j) == (i, columna):
                continue
            if not grafo.estan_unidos((i, j), (i, columna)):
                grafo.agregar_arista((i, j), (i, columna))
        
        # Agrego aristas a la columna
        for fila in range(n):
            if (i, j) == (fila, j):
                continue
            if not grafo.estan_unidos((i, j), (fila, j)):
                grafo.agregar_arista((i, j), (fila, j))
        
        # Agrego aristas en las diagonales
        agregar_diagonales(grafo, i, j, n)

    return grafo

def agregar_diagonales(grafo, i, j, n):
    for num in range(1, n):
        agregar_diagonal(grafo, (i,j), i+num, j+num, n)
        agregar_diagonal(grafo, (i,j), i-num, j-num, n)
        agregar_diagonal(grafo, (i,j), i-num, j+num, n)
        agregar_diagonal(grafo, (i,j), i+num, j-num, n)

def agregar_diagonal(grafo, vertice, x, y , n):
    if not estoy_en_rango(x, y, n):
        return
    
    if not grafo.estan_unidos(vertice, (x, y)):
        grafo.agregar_arista(vertice, (x, y))

def estoy_en_rango(x, y, n):
    cond1 = x >= 0 and y >= 0
    cond2 =  x < n and y < n

    return cond1 and cond2

def probar_nreinas(n):
    grafo, resultado = nreinas(n)
    columna = 0
    for vertice in grafo:
        if columna == n:
            print("")
            columna = 0

        columna += 1
        if vertice in resultado:
            print(" REINA \t", end="")
        else:
            print(f"{vertice}\t", end="")
    print("")

probar_nreinas(12)