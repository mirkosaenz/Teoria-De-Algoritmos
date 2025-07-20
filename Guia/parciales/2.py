def asignar_proyectos(proyectos, grupos):
    asignados = []
    for i in range(grupos):
        asignados.append([])

    solucion, cantidad = _asignar(proyectos, 0, asignados, 0, asignados, 0)
    return solucion

def _asignar(proyectos, actual, mejor_asig, k_asig, asig_act, k_act):
    if not ultimo_cumple(asig_act, proyectos, actual):
        return mejor_asig, k_asig
    
    if actual == len(proyectos):
        if k_act > k_asig:
            resultado = []
            for grupo in asig_act:
                resultado.append(grupo.copy())
            return resultado, k_act
        
        return mejor_asig, k_asig

    proyecto = proyectos[actual]
    mejor = mejor_asig
    k = k_asig

    for grupo in asig_act:
        grupo.append(proyecto)
        mejor, k = _asignar(proyectos, actual+1, mejor, k, asig_act, k_act+1)
        grupo.pop()
    
    mejor, k = _asignar(proyectos, actual+1, mejor, k, asig_act, k_act)

    return mejor, k

def ultimo_cumple(asig_act, proyectos, actual):
    if actual == 0:
        return True
    
    proyecto = proyectos[actual-1]
    grupo_proyecto = None
    
    # Busco si esta en algun grupo
    for grupo in asig_act:
        if proyecto in grupo:
            grupo_proyecto = grupo
            break
    
    # Si no esta en ningun grupo, cumple
    if grupo_proyecto is None:
        return True
    
    # Busco que no solape
    for otro_proy in grupo_proyecto:
        if proyecto == otro_proy:
            continue

        if proyecto[0] < otro_proy[1]:
            return False
    
    return True

print(asignar_proyectos([(1,5), (1, 3), (2, 4), (5, 6), (0, 3)], 2))