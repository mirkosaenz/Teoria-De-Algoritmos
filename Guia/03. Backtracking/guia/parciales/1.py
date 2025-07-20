def asignar_proyectos(proyectos, k):
    inicios = [0]*k
    grupos = []

    for i in range(len(inicios)):
        grupos.append([])

    proyectos = sorted(proyectos, key=lambda x: x[1])

    for proyecto in proyectos:
        ini, fin = proyecto

        for i in range(len(inicios)):
            if ini >= inicios[i]:
                grupos[i].append(proyecto)
                inicios[i] = fin
                break
    
    return grupos

print(asignar_proyectos([(1,5), (1, 3), (2, 4), (5, 6), (0, 3)], 2))