from ff import ford_fulkerson
from grafo import Grafo
import math

MAX_DISTANCIA = 3

def asignar_ambulancias(ambulancias, pedidos):
    red = crear_red(ambulancias, pedidos, MAX_DISTANCIA)
    asignaciones = {}
    flujos = ford_fulkerson(red)

    for pedido in pedidos:
        for posible_amb in red.adyacentes(pedido):
            arista = (pedido, posible_amb)
            if flujos[arista] == 1:
                asignaciones[pedido] = posible_amb
                break
    
    return asignaciones

def crear_red(ambulancias, pedidos, k):
    red = Grafo(es_dirigido=True)
    red.agregar_vertice("T")

    for ambulancia in ambulancias:
        red.agregar_vertice(ambulancia)
        red.agregar_arista(ambulancia, "T", peso=1)
    
    red.agregar_vertice("S")
    for pedido in pedidos:
        red.agregar_vertice(pedido)
        red.agregar_arista("S", pedido, peso=1)
    
    for amb in ambulancias:
        if dist(pedido, amb) < k:
            red.agregar_arista(pedido, amb, peso=1)
    
    return red

def dist(pedido, ambulancia):
    x1, y1 = pedido
    x2, y2 = ambulancia
    resta = (x2-x1, y2-y1)
    x, y = resta
    return math.sqrt(x*x+y*y)