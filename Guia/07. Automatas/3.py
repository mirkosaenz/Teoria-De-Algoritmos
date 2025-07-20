def es_parte_lenguaje(cadena):
    # Como minimo se necesita pasar por dos estados para llegar
    # a un estado de aceptacion
    if len(cadena) < 2:
        return False
    
    # Si la cadena empieza con "ac" va a ser aceptada
    if cadena[0] == "a" and cadena[1] == "c":
        return True

    # Si la cadena termina con "ab" va a ser aceptada
    if cadena[len(cadena)-2] == "a" and cadena[len(cadena)-1] == "b":
        return True

    # Sino la cadena es rechazada
    return False