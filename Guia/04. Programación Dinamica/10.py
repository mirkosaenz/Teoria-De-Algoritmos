def plan_operativo(arreglo_L, arreglo_C, costo_M):
    if len(arreglo_L) == 0:
        return []
    
    M = [0]*len(arreglo_L)
    OPTL, OPTC = costos_ciudad(arreglo_L, arreglo_C, costo_M)

    valor_ultimo = min(OPTL[-1], OPTC[-1])
    ultimo = "londres" if valor_ultimo == OPTL[-1] else "california"

    return reconstruir(arreglo_L, arreglo_C, OPTL, OPTC, ultimo, valor_ultimo, costo_M)

def reconstruir(l, c, OPTL, OPTC, ultimo, valor_ultimo, costo_M):
    i = len(OPTL) - 1
    resultado = []
    valor_actual = valor_ultimo
    actual = ultimo

    while i >= 0:
        resultado.append(actual)
        if valor_actual == OPTL[i]:
            if valor_actual == OPTL[i-1]+l[i]:
                valor_actual = OPTL[i-1]
            else:
                valor_actual = OPTC[i-1]
                actual = "california"

        if valor_actual == OPTC[i]:
            if valor_actual == OPTC[i-1]+c[i]:
                valor_actual = OPTC[i-1]
            else:
                valor_actual = OPTL[i-1]
                actual = "londres"
        
        i -= 1
    
    resultado.reverse()
    return resultado
    
def costos_ciudad(arreglo_L, arreglo_C, costo_M):    
    OPTL = [0]*(len(arreglo_L))
    OPTC = [0]*(len(arreglo_C))

    OPTL[0] = arreglo_L[0]
    OPTC[0] = arreglo_C[0]

    for i in range(1, len(arreglo_L)):
        OPTL[i] = min(OPTL[i-1]+arreglo_L[i], OPTC[i-1]+arreglo_L[i]+costo_M)
        OPTC[i] = min(OPTC[i-1]+arreglo_C[i], OPTL[i-1]+arreglo_C[i]+costo_M)
    
    return OPTL, OPTC

print(plan_operativo([20,10,20], [30,5,20], 4))