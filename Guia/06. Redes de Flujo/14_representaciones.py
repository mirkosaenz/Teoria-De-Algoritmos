from grafo import Grafo
from ff import ford_fulkerson

def crear_red_flujo(clubes, partidos, habitantes):
    red = Grafo(es_dirigido=True)
    for club in clubes: red.agregar_vertice(club)
    for partido in partidos: red.agregar_vertice(partido)

    for hab in habitantes:
        nombre, clubes_hab, partido = hab
        red.agregar_vertice(nombre)

        for club in clubes_hab:
            red.agregar_arista(club, nombre, peso=1)
        
        red.agregar_arista(nombre, partido, peso=1)
    
    red.agregar_vertice("S") #Fuente
    red.agregar_vertice("T") #Sumidero

    for club in clubes:
        red.agregar_arista("S", club, peso=1)
    
    for partido in partidos:
        red.agregar_arista(partido, "T", peso=(len(habitantes) // 2))

    return red


def obtener_representantes(habitantes):
    clubes, partidos = set(), set()
    for hab in habitantes:
        nombre, clubes_hab, partido = hab
        
        for club in clubes_hab:
            clubes.add(club)

        partidos.add(partido)
    
    red = crear_red_flujo(clubes, partidos, habitantes)
    flujo = ford_fulkerson(red)

    representantes = []
    for club in clubes:
        for nombre in red.adyacentes(club):
            arista = (club, nombre)
            if arista in flujo and flujo[arista] == 1:
                representantes.append(arista)

    return representantes

def main():
    archivo = open("datos/datos_14.txt", "r")
    habitantes = []
    
    for linea in archivo:
        linea = linea.strip()
        nombre, clubes, pp = linea.split(",")
        clubes = clubes.split("-")
        habitantes.append((nombre, clubes, pp))

    representantes = obtener_representantes(habitantes)
    for representacion in representantes:
        club, nombre = representacion
        print(f"El representante de {club} sera {nombre}")

main()