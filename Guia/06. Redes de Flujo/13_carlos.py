from grafo import Grafo
from ff import ford_fulkerson

def transformar_ciudad_en_red(ciudad:Grafo, casa, escuela):
    """
    PRE: 
    -   Recibe un grafo dirigido, que se pretende convertir en red de flujo.
    -   La ciudad esta en una sola CFC (no hay esquinas sin entrada o salida)
    
    POST -> Devuelve:
    -   Una red de flujo donde la casa es la fuente y la escuela el sumidero    
    -   Un set con los vertices ficticios agregados para convertir ciclos de 2 en ciclos de 3
    """
    red = Grafo(es_dirigido=True)
    ficticios = set()

    for vertice in ciudad:
        if not vertice in red:
            red.agregar_vertice(vertice)

        for ady in ciudad.adyacentes(vertice):
            # Quiero que la casa tenga grado de entrada 0 (va a ser la fuente)
            if ady == casa: 
                continue

            # Si no agregue el ady a la red, lo agrego
            if not ady in red:
                red.agregar_vertice(ady)
            
            # Si ya estan unidos, contemple las dos aristas posibles.
            if red.estan_unidos(vertice, ady):
                continue

            # Agrego la arista de ida
            red.agregar_arista(vertice, ady, 1)

            # Si existe arista de vuelta, la agrego con vertice intermedio
            # i.e convierto ciclo de 2 en ciclo de 3
            # solamente si el vertice NO es la casa
            if ciudad.estan_unidos(ady, vertice) and vertice != casa:
                intermedio = f"{ady}-{vertice}"
                red.agregar_vertice(intermedio)
                ficticios.add(intermedio)

                # Conecto el ady al intermedio, y el intermedio al actual
                red.agregar_arista(ady, intermedio, 1)
                red.agregar_arista(intermedio, vertice, 1)
    
    # Elimino las aristas salientes de la escuela (va a ser el sumidero)
    adyacentes_escuela = ciudad.adyacentes(escuela)
    for ady in adyacentes_escuela:
        red.borrar_arista(escuela, ady)
    
    return red, ficticios

def reconstruir_caminos(red:Grafo, flujo, casa, escuela, ficticios):
    caminos = []

    # Resuelvo situacion con vertices ficticios
    for ficticio in ficticios:
        origen, destino = ficticio.split("-")
        aristas_ciclo = [(origen, ficticio), (ficticio, destino), (destino, origen)]
        
        # Si va y vuelve flujo, que cada uno siga por donde continuaba el otro
        if flujo[(destino, origen)] == 1 and flujo[origen, ficticio] == 1:
            for arista in aristas_ciclo:
                red.borrar_arista(arista[0], arista[1])

    cam_actual = []
    while cam_actual != None:
        actual = casa

        while actual != escuela:
            if actual not in ficticios:
                cam_actual.append(actual)
            
            sig = None
            for ady in red.adyacentes(actual):
                if flujo[(actual, ady)] == 1:
                    sig = ady
                    flujo[(actual, ady)] = 0 # Para no contemplarlo en siguientes iteraciones
                    break
            
            if sig == None:
                cam_actual = None
                break

            actual = sig

        # Si no encontre una arista con peso 1, ya no hay caminos restantes
        if cam_actual == None:
            break
        
        cam_actual.append(escuela)
        caminos.append(cam_actual)
        cam_actual = []

    return caminos

def problema_carlos(ciudad:Grafo, casa, escuela, cant_hijos):
    red, ficticios = transformar_ciudad_en_red(ciudad, casa, escuela)
    flujo = ford_fulkerson(red)

    caminos = reconstruir_caminos(red, flujo, casa, escuela, ficticios)

    return len(caminos) >= cant_hijos, caminos

def main():
    vertices = ["A", "B", "C", "D", "E", "F"]
    aristas = [("A", "B"), ("A", "C"), ("B", "C"), ("C", "B"), ("B", "D"), ("C", "D"), ("A", "E"), ("E", "D"), ("A", "F"), ("F", "D")]
    grafo = Grafo(es_dirigido=True, vertices=vertices)

    for arista in aristas:
        origen, destino = arista
        grafo.agregar_arista(origen, destino)

    caminos = problema_carlos(grafo, "A", "D", 3)
    print(caminos)

main()