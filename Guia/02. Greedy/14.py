from grafo import Grafo

# devolver una lista de faros. Cada faro debe ser una tupla con su posición en (x,y)
# matriz booleana, indica True en las posiciones con submarinos
def submarinos(matriz):
    grafo = armar_grafo(matriz)
    iluminados = set()
    faros = []

    for i, j in grafo.obtener_vertices():
        # Si hay un submarino y esa posicion todavia no esta iluminada
        if matriz[i][j] and (i, j) not in iluminados:
            cant_iluminados = 1
            iluminados_actual = [(i, j)]
            faro_actual = (i, j)
            
            for ady in grafo.adyacentes((i, j)):
                iluminados_ady = obtener_iluminados(grafo, ady, matriz)
                
                if len(iluminados_ady) > cant_iluminados:
                    cant_iluminados = len(iluminados_ady)
                    iluminados_actual = iluminados_ady
                    faro_actual = ady
            
            faros.append(faro_actual)
            for iluminado in iluminados_actual:
                iluminados.add(iluminado)
    
    return faros

def armar_grafo(matriz):
    grafo = Grafo(es_dirigido=False)

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            grafo.agregar_vertice((i,j))
    
    for i, j in grafo.obtener_vertices():
        for fila in range(i-2, i+3):
            for columna in range(j-2, j+3):
                cond1 = fila > 0 and fila < len(matriz)
                cond2 = columna > 0 and columna < len(matriz[0])
                cond3 = not grafo.estan_unidos((i, j), (fila, columna))

                if cond1 and cond2 and cond3:
                    grafo.agregar_arista((i, j), (fila, columna)) 
    
    return grafo

def obtener_iluminados(grafo, vertice, matriz):
    iluminados = []

    for ady in grafo.adyacentes(vertice):
        i, j = ady 
        if matriz[i][j]:
            iluminados.append((i, j))
    
    return iluminados