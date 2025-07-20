def resolver_sudoku(matriz):
    subgrupos = armar_subgrupos(matriz)
    return _resolver_sudoku(matriz, subgrupos, (0,0))

def _resolver_sudoku(matriz, subgrupos, pos_actual):
    # Siempre mando la sig posicion sumando a la columna.
    # Si me pase, voy a la sig fila.
    if pos_actual[1] == len(matriz):
        pos_actual = (pos_actual[0]+1, 0)
    
    pos_me_pase = (len(matriz), 0)

    if pos_actual == pos_me_pase:
        return matriz if ultimo_cumple(matriz, pos_actual, subgrupos) else None
    
    if not ultimo_cumple(matriz, pos_actual, subgrupos):
        return None
    
    i, j = pos_actual
    # Si el vertice ya tiene un valor asignado por defecto, voy al sig.
    if matriz[i][j] != 0:
        return _resolver_sudoku(matriz, subgrupos, (i, j+1))
    
    for n in range(1, 10):
        matriz[i][j] = n
        resultado = _resolver_sudoku(matriz, subgrupos, (i, j+1))
        if resultado is not None:
            return resultado

    matriz[i][j] = 0
    return None

def ultimo_cumple(matriz, pos_actual, subgrupos):
    if pos_actual == (0,0):
        return True
    
    # Calculo la pos del anterior sabiendo pos_actual
    pos_anterior = (pos_actual[0], pos_actual[1]-1)
    if pos_anterior[1] < 0:
        pos_anterior = (pos_actual[0]-1, len(matriz)-1) 

    i, j = pos_anterior
    grupo_actual = obtener_subgrupo((i, j))
    
    for n in range(len(matriz)):
        if n != i and matriz[i][j] == matriz[n][j]:
            return False
        if n != j and matriz[i][j] == matriz[i][n]:
            return False

    for celda_grupo in subgrupos[grupo_actual]:
        k, m = celda_grupo
        if (i, j) == (k, m):
            continue
        if matriz[i][j] == matriz[k][m]:
            return False
    
    return True

def armar_subgrupos(matriz):
    # Dicc del formato subgrupo: celdas q componen
    subgrupos = {}
    
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            grupo = (i // 3, j // 3)
            
            if not grupo in subgrupos:
                subgrupos[grupo] = []

            subgrupos[grupo].append((i, j))
    
    return subgrupos

def obtener_subgrupo(pos):
    i ,j = pos
    return (i // 3, j // 3)