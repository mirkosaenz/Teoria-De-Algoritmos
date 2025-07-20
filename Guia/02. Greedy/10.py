def bifurcaciones_con_patrulla(ciudades):
    ciudades = sorted(ciudades, key=lambda x: x[1])
    controles = []
    ciudades_controles = []

    for ciudad in ciudades:
        # Si no hay ningun control, agrego uno
        if len(controles) == 0:
            controles.append(ciudad)
            ciudades_controles.append([ciudad])
            continue

        ciudades_ult_control = ciudades_controles[len(ciudades_controles)-1]
        control_actual = controles[len(controles)-1]

        # Si el control actual no me alcanza, tengo que crear uno nuevo
        if control_actual[1] + 50 < ciudad[1]:
            controles.append(ciudad)
            ciudades_controles.append([ciudad])
        # Si el control alcanza, me agrego
        else:
            ciudades_ult_control.append(ciudad)

            # Si la ciudad actual puede controlar todas las del control, cambio el control a esta ciudad
            if ciudad[1]-50 <= ciudades_ult_control[0][1]:
                controles.pop()
                controles.append(ciudad)
    
    return controles

print(bifurcaciones_con_patrulla([("Nombre", 156), ("Nombre 2", 185), ("Nombre 3", 185), ("Nombre 4", 242), ("Nombre 5", 270)]))