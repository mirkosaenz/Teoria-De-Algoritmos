def nreinas(n):
    cols_posibles = set(i for i in range(n))
    fila_actual = 0
    
    resultado = _n_reinas(cols_posibles, fila_actual, [], n)
    if resultado != None:
        return resultado
    
    return []

def _n_reinas(cols_posibles, fila, reinas, n):
    if len(reinas) == n:
        return reinas if ultima_cumple(reinas, n) else None
    
    if fila == n:
        return None
    
    if not ultima_cumple(reinas, n):
        return None
    
    # Para no volver a iterar una columna cuando la saque y volvi a agregar
    lista_columnas = list(cols_posibles)
    
    # Pruebo las diferentes opciones para la decision
    for columna in lista_columnas:
        # Asigno esa col a la fila actual y la saco de las posibles (criba)
        reinas.append((fila, columna))
        cols_posibles.remove(columna)
        
        resultado = _n_reinas(cols_posibles, fila+1, reinas, n)
        if resultado != None:
            return resultado
        
        reinas.pop()
        cols_posibles.add(columna)
    
    return None

def ultima_cumple(reinas, n):
    if len(reinas) == 0:
        return True
    
    ultima = reinas[len(reinas)-1]
    for reina in reinas:
        if reina == ultima:
            continue
        if se_matan(reina, ultima, n):
            return False
    
    return True

def se_matan(reina1, reina2, n):
    x1, y1 = reina1
    x2, y2 = reina2

    if x1 == x2 or y1 == y2:
        return True
    
    for i in range(1, n):
        diagonales = [
            (x1-i, y1+i), (x1+i, y1+i), 
            (x1-i, y1-i), (x1+i, y1-i)
        ]

        for diag in diagonales:
            if diag == reina2:
                return True

    return False

print(nreinas(8))