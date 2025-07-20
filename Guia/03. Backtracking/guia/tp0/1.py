alumnos = [1.2, 1.15, 1.14, 1.12, 1.02, 0.98]

def indice_mas_bajo(alumnos):
    return _indice_mas_bajo(alumnos, 0, len(alumnos))

def _indice_mas_bajo(alumnos, desde, hasta):
    if desde >= hasta:
        return -1 # Solo ocurriria si el arreglo no cumple la precondicion
    
    mitad = int((desde + hasta) / 2)

    if validar_mas_bajo(alumnos, mitad):
        return mitad
    
    if alumnos[mitad-1] > alumnos[mitad]:
        return _indice_mas_bajo(alumnos, mitad+1, hasta)
    
    return _indice_mas_bajo(alumnos, desde, mitad)


def validar_mas_bajo(alumnos, indice):
    if indice > 0 and alumnos[indice-1] < alumnos[indice]:
        return False
    
    if indice < len(alumnos)-1 and alumnos[indice+1] < alumnos[indice]:
        return False
    
    return True
