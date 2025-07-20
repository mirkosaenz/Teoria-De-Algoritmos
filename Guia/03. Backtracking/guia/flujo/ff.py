from grafo import Grafo
from collections import deque as Cola

def copiar_grafo(anterior:Grafo):
    nuevo = Grafo(es_dirigido=True ,vertices=anterior.obtener_vertices())

    for vertice in anterior:
        for ady in anterior.adyacentes(vertice):
            nuevo.agregar_arista(vertice, ady, peso=anterior.peso_arista(vertice, ady))

    return nuevo

def grados_entrada(grafo):
    grados = {}
    for vertice in grafo:
        grados[vertice] = 0
    
    for vertice in grafo:
        for ady in grafo.adyacentes(vertice):
            grados[ady] += 1

    return grados

def grados_salida(grafo):
    grados = {}
    
    for vertice in grafo:
        grados[vertice] = len(grafo.adyacentes(vertice))

    return grados

def buscar_fuente_y_sumidero(red):
    fuente = None
    sumidero = None
    gr_entrada = grados_entrada(red)
    gr_salida = grados_salida(red)
    
    for vertice in red:
        if gr_entrada[vertice] == 0:
            fuente = vertice
        elif gr_salida[vertice] == 0:
            sumidero = vertice
        
        if fuente and sumidero:
            return fuente, sumidero
    
    return fuente, sumidero

def buscar_flujo_max(red_residual, camino):
    flujo = float("inf")
    
    for arista in camino:
        origen, dest = arista
        peso = red_residual.peso_arista(origen, dest)
        if peso < flujo:
            flujo = peso

    return flujo

def buscar_camino(grafo, fuente, sumidero):
    cola = Cola()
    padres = {}
    visitados = set()

    cola.append(fuente)
    visitados.add(fuente)
    
    while not len(cola) == 0:
        actual = cola.popleft()

        for ady in grafo.adyacentes(actual):
            if ady in visitados:
                continue
            if ady == sumidero:
                padres[sumidero] = actual
                return reconstruir_camino(grafo, padres, fuente, sumidero)
            
            visitados.add(ady)
            padres[ady] = actual
            cola.append(ady)
    
    return None

def reconstruir_camino(grafo, padres, fuente, sumidero):
    camino = []
    actual = sumidero
    
    while padres[actual] != fuente:
        camino.append((padres[actual], actual))
        actual = padres[actual]
    camino.append((padres[actual], actual))

    return camino[::-1]

def actualizar_red_residual(red:Grafo, origen, dest, flujo):
    # Le resto el flujo disponible a la arista actual (o idem al reves)
    peso_original = red.peso_arista(origen, dest)
    peso_nuevo = peso_original-flujo
    if peso_nuevo == 0:
        red.borrar_arista(origen, dest)
    else:
        red.actualizar_arista(origen, dest, peso_original-flujo)


    # Le sumo el flujo utilizado a la arista opuesta (o idem al reves)
    if not origen in red.adyacentes(dest):
        red.agregar_arista(dest, origen, 0)
    
    peso_opuesta = red.peso_arista(dest, origen)
    red.actualizar_arista(dest, origen, peso_opuesta+flujo)

def obtener_flujos(red_original, red_residual):
    flujos = {}

    for vertice in red_residual:
        for ady in red_residual.adyacentes(vertice):
            # Si esta en la red original no es antiparalela.
            # Por lo tanto, no es la que carga el flujo
            if red_original.estan_unidos(vertice, ady):
                if (vertice, ady) not in flujos:
                    flujos[(vertice, ady)] = 0 # Inicializo en 0
                continue
            
            # Si es antiparalela, tiene el flujo que carga la opuesta
            arista_original = (ady, vertice)
            flujos[arista_original] = red_residual.peso_arista(vertice, ady)
            
    
    return flujos

def ford_fulkerson(red_original):
    red_residual = copiar_grafo(red_original)
    fuente, sumidero = buscar_fuente_y_sumidero(red_original)

    camino = buscar_camino(red_residual, fuente, sumidero)
    while camino:
        flujo = buscar_flujo_max(red_residual, camino)
        
        for arista in camino:
            origen, dest = arista
            actualizar_red_residual(red_residual, origen, dest, flujo)
        
        camino = buscar_camino(red_residual, fuente, sumidero)
    
    flujos = obtener_flujos(red_original, red_residual)
    return flujos
