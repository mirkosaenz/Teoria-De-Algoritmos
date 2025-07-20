def cambio(monedas, monto):
    monedas = sorted(monedas)
    if monto == 0:
        return []
    
    M = [0]*(monto+1)
    M[0] = 0

    for i in range(1, monto+1):
        monedas_posibles = obtener_monedas_posibles(monedas, i)
        
        M[i] = 1 + min([M[i-moneda] for moneda in monedas_posibles])
    
    return reconstruir(monedas, M)

def reconstruir(monedas, M):
    resultado = []
    
    monto = len(M)-1

    while monto > 0:
        minimo = float("inf")
        moneda_min = -1
        
        # Checkeo con cual moneda me quedo mejor solucion para esta cantidad
        for moneda in obtener_monedas_posibles(monedas, monto):
            if M[monto-moneda] < minimo:
                minimo = M[monto-moneda]
                moneda_min = moneda 
        
        # Guardo la moneda que mejoro mi solucion
        resultado.append(moneda_min)

        # Sigo buscando cual moneda puse antes que la de recien
        monto = monto - moneda_min
    
    resultado.reverse()
    return resultado

def obtener_monedas_posibles(monedas, monto):
    monedas_posibles = []

    for moneda in monedas:
        if moneda <= monto:
            monedas_posibles.append(moneda)
    
    return monedas_posibles