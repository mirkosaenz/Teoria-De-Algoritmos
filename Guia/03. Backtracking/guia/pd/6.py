from grafo import Grafo

def numeros_posibles(k, n):
    resultado = []
    resultado.append([0]*10)
    grafo = armar_grafo()

    for i in range(1, n+1):
        caminos = []

        for j in range(10):
            if i == 1:
                caminos.append(1)
                continue
            
            cantidad = 1
            for ady in grafo.adyacentes(j):
                for r in range(i):
                    cantidad += resultado[r][ady]
        
            caminos.append(cantidad)
        
        resultado.append(caminos)
    return resultado[n][k]

def armar_grafo():
    matriz = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [-1, 0, -1]
    ]
    grafo = Grafo(es_dirigido=False)

    for i in range(10):
        grafo.agregar_vertice(i)
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == -1:
                continue
            direcciones = [
                (i-1, j), (i+1, j),
                (i, j-1), (i, j+1)
            ]

            for fil, col in direcciones:
                if not en_rango(matriz, fil, col) or matriz[fil][col] == -1:
                    continue
                if not grafo.estan_unidos(matriz[i][j], matriz[fil][col]):
                    grafo.agregar_arista(matriz[i][j], matriz[fil][col])
    
    return grafo


def en_rango(matriz, fil, col):
    cond1 = fil >= 0 and col >= 0
    cond2 = fil < len(matriz) and col < len(matriz[0])

    return cond1 and cond2