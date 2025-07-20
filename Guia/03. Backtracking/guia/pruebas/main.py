from grafo import Grafo

def main():
    vertices = ["A", "B", "C"]
    grafo = Grafo(vertices=vertices)

    grafo.agregar_arista("A", "B")
    grafo.agregar_arista("A", "C")
    for vertice in grafo:
        print(vertice)
    
    vertices = grafo.obtener_vertices()
    print(vertices)


main()